// Reference preflight, not a hypothesis test. Node: node <this file>.
function run(){
 const D={"0011":"1","0101":"2","1001":"3","0000":"4","1100":"5","1010":"6","0110":"7","1111":"8"}, lab=w=>D[w]||"0",phi=w=>String((54>>parseInt(w,2))&1),tab={};
 for(let i=0;i<64;i++){let w=i.toString(2).padStart(6,"0"),z=[0,1,2].map(j=>lab(w.slice(j,j+4))).join(""),v=lab([0,1,2,3].map(j=>phi(w.slice(j,j+3))).join(""));if(z in tab&&tab[z]!==v)throw Error("closure");tab[z]=v}
 const filt=x=>Array.from({length:x.length-3},(_,i)=>lab(x.slice(i,i+4))).join("");
 const micro=x=>Array.from({length:x.length-2},(_,i)=>phi(x.slice(i,i+3))).join("");
 const step=z=>Array.from(z,(_,i)=>{let k=(z[i-1]||"0")+z[i]+(z[i+1]||"0");if(!(k in tab))throw Error(k);return tab[k]}).join("");
 function decode(z){let xs=Array.from({length:8},(_,i)=>i.toString(2).padStart(3,"0"));for(let a of z)xs=xs.flatMap(x=>["0","1"].filter(b=>lab(x.slice(-3)+b)===a).map(b=>x+b));return xs}
 const seed="53108880", sparse=(z,c)=>Array.from(z,(a,i)=>a==="0"?null:[i-c,a]).filter(Boolean);
 const core=[[-4,"5"],[-3,"3"],[-2,"1"],[0,"8"],[1,"8"],[2,"8"]],eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 function decompose(z,c,odd){
  let s=sparse(z,c),inside=s.filter(([i])=>i>=-4&&i<=3),left=s.filter(([i])=>i< -4),right=s.filter(([i])=>i>3);
  if(!odd){left=s.filter(([i])=>i<0);right=s.filter(([i])=>i>=0);inside=[]}
  const sep=(a)=>a.every(([i],j)=>j===0||i-a[j-1][0]>=3);
  const ok=eq(inside,odd?core:[])&&left.every(([i,a])=>["1","6"].includes(a))&&right.every(([i,a])=>["2","5"].includes(a))&&sep(left)&&sep(right)&&(odd?left.every(([i])=>i<=-7)&&right.every(([i])=>i>=5):!left.length||!right.length||right[0][0]-left.at(-1)[0]>=3);
  return {ok,inside,left,right}
 }
 const cases=[];let comparisons=0;
 for(let n=1;n<=24;n++){
  const checkpoint=n%2?6*(n-1)+32:6*n+16,h=checkpoint+32,p=2*h+16,c=p+4*n;
  let z="0".repeat(p)+seed.repeat(n)+"0".repeat(p),xs=decode(z);
  if(xs.length!==1){cases.push({n,decodeCount:xs.length,failed:"decode"});continue}
  let x=xs[0],failures=[],at={},first32=[];
  for(let t=0;t<=h;t++){
   comparisons++;if(filt(x)!==z.slice(t,z.length-t))failures.push(t);
   if(n===1&&t<=32)first32.push(sparse(z,c));
   if(t===checkpoint||t===h)at[t]=decompose(z,c,n%2===1);
   if(t<h){x=micro(x);z=step(z)}
  }
  cases.push({n,checkpoint,h,p,decodeCount:xs.length,initialRaw:xs[0],failures,at,...(n===1?{first32}:{})})
 }
 // Test elementary movers and all-zero quiescence, independently of gun recurrence.
 let movers={};for(const a of ["1","6","2","5"]){let z="000"+a+"000";movers[a]=sparse(step(z),3)}
 return {version:"reference-preflight-v1",scope:"engineered secondary-domain parity, n=1..24, finite cone; no seeds",comparisons,movers,zero:sparse(step("0000000"),3),summary:{cases:cases.length,rawMatches:cases.filter(c=>c.failures?.length===0).length,parityMatches:cases.filter(c=>Object.values(c.at||{}).length===2&&Object.values(c.at).every(a=>a.ok)).length},cases}
}
console.log(JSON.stringify(run()));
