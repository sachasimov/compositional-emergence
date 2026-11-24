// Rule 54 reference preflight; Hanson & Crutchfield (1997), Fig. 5 and section 4.3.
function run(){
 // Fig. 5, state is trailing three bits; label on rightmost site.
 const labels={"0011":"1","0101":"2","1001":"3","0000":"4","1100":"5","1010":"6","0110":"7","1111":"8"};
 const bits=(k,n)=>k.toString(2).padStart(n,"0");
 const label=w=>labels[w]||"0";
 const phi=w=>String((54>>parseInt(w,2))&1);
 const idx=(s,i)=>s[((i%s.length)+s.length)%s.length];
 const word=(s,i,n)=>Array.from({length:n},(_,j)=>idx(s,i+j)).join("");
 const T=s=>Array.from({length:s.length},(_,i)=>label(word(s,i-3,4))).join("");
 const step=s=>Array.from({length:s.length},(_,i)=>phi(word(s,i-1,3))).join("");
 const mask=z=>z.replace(/[1-8]/g,"1");
 const table={},radius0={},r0conflicts=[],localRows=[];
 for(let k=0;k<64;k++){
  const x=bits(k,6),z=[0,1,2].map(i=>label(x.slice(i,i+4))).join("");
  const y=[0,1,2,3].map(i=>phi(x.slice(i,i+3))).join(""),out=label(y);
  if(z in table && table[z]!==out)throw Error("radius-one conflict "+z);
  table[z]=out;
  if(z[1] in radius0 && radius0[z[1]].out!==out)r0conflicts.push({first:radius0[z[1]],second:{x,z,out}});
  else if(!(z[1] in radius0))radius0[z[1]]={x,z,out};
  localRows.push({x,z,y,out});
 }
 const decode=z=>{
  const i=[...z].findIndex(x=>x!=="0");
  if(i<0)return null;
  const rev=Object.fromEntries(Object.entries(labels).map(([w,l])=>[l,w]));
  let w=rev[z[i]],last=w.slice(1),s=Array(z.length);
  s[i]=w[3];
  for(let j=1;j<z.length;j++){
   const l=z[(i+j)%z.length];
   const next=l==="0"?String(1^Number(last[0])^Number(last[1])^Number(last[2])):rev[l][3];
   if(label(last+next)!==l)throw Error("invalid transition");
   s[(i+j)%z.length]=next;last=last.slice(1)+next;
  }
  const raw=s.join("");if(T(raw)!==z)throw Error("invalid decoded row");return raw;
 };
 const sizes=[],parityWitnesses=[];
 for(let n=4;n<=12;n++){
  const fibers=new Map(),masks=new Map();let zero=0,decodeChecked=0,localChecked=0,reflectionChecked=0,parityConflicts=0,witness=null;
  for(let k=0;k<2**n;k++){
   const x=bits(k,n),z=T(x),next=T(step(x)),m=mask(z),mnext=mask(next);
   fibers.set(z,(fibers.get(z)||0)+1);
   const pred=Array.from({length:n},(_,i)=>table[word(z,i-1,3)]).join("");
   if(pred!==next)throw Error("ring closure");
   localChecked++;
   const reflect=[...x].reverse().join("");
   const p={"0":"0","1":"5","2":"6","3":"3","4":"4","5":"1","6":"2","7":"7","8":"8"};
   const reflected=Array.from({length:n},(_,i)=>p[idx(z,n-1-i+3)]).join("");
   if(T(reflect)!==reflected)throw Error("reflection");
   reflectionChecked++;
   if(z.includes("1")||/[2-8]/.test(z)){if(decode(z)!==x)throw Error("decode");decodeChecked++}else{zero++;if(next!=="0".repeat(n))throw Error("domain invariance")}
   if(masks.has(m)&&masks.get(m).mnext!==mnext){parityConflicts++;if(!witness)witness={first:masks.get(m),second:{x,z,m,mnext},n}}else if(!masks.has(m))masks.set(m,{x,z,m,mnext});
  }
  const hist={};for(const v of fibers.values())hist[v]=(hist[v]||0)+1;
  const nonzeroCollisions=[...fibers.entries()].filter(([z,c])=>c>1&&/[1-8]/.test(z)).length;
  if(nonzeroCollisions||zero!==(n%4===0?8:0))throw Error("fiber counts");
  sizes.push({n,total:2**n,zero,decodeChecked,localChecked,reflectionChecked,distinctTyped:fibers.size,fiberHistogram:hist,distinctMasks:masks.size,parityConflicts});
  if(witness)parityWitnesses.push(witness);
 }
 return {labels,localRows,table,admissibleTriples:Object.keys(table).length,radius0ConflictCount:r0conflicts.length,radius0Witness:r0conflicts[0],sizes,parityWitnesses};
}
console.log(JSON.stringify(run(),null,2));
