function run(){
 const D={"0011":"1","0101":"2","1001":"3","0000":"4","1100":"5","1010":"6","0110":"7","1111":"8"},lab=w=>D[w]||"0",phi=w=>String((54>>parseInt(w,2))&1);
 const tab={};
 for(let i=0;i<64;i++){let w=i.toString(2).padStart(6,"0"),z=[0,1,2].map(j=>lab(w.slice(j,j+4))).join(""),v=lab([0,1,2,3].map(j=>phi(w.slice(j,j+3))).join(""));if(z in tab&&tab[z]!==v)throw Error("closure");tab[z]=v}
 const filt=x=>Array.from({length:x.length-3},(_,i)=>lab(x.slice(i,i+4))).join("");
 const micro=x=>Array.from({length:x.length-2},(_,i)=>phi(x.slice(i,i+3))).join("");
 const step=z=>Array.from(z,(_,i)=>{let k=(z[i-1]||"0")+z[i]+(z[i+1]||"0");if(!(k in tab))throw Error(k);return tab[k]}).join("");
 // Construct the raw block directly: n+3 consecutive ones. Extend each
 // side by the odd four-bit parity condition of the published pure domain.
 function raw(n,p){let x="1".repeat(n+3);for(let i=0;i<p;i++){let a=x.slice(0,3),b=x.slice(-3);x=String(1^+a[0]^+a[1]^+a[2])+x+String(1^+b[0]^+b[1]^+b[2])}return x}
 const strip=z=>z.replace(/^0+|0+$/g,""),A="(?:444|50401|3|888)",B="(?:44|5001|26|88)";
 const classify=s=>s===""?"empty":new RegExp("^"+B+"$").test(s)?"B":new RegExp("^"+A+"$").test(s)?"A":new RegExp("^[16]0+"+A+"0+[25]$").test(s)?"LAR":"unresolved";
 const paper=["B","A","empty","LAR"],candidate=["empty","LAR","B","A"];
 let cases=[],checks=0,reductionChecks=0;
 for(let n=1;n<=64;n++){let h=n+24,p=2*h+16,x=raw(n,p),z="0".repeat(p)+"8".repeat(n)+"0".repeat(p),frames=[],ok=true,red=true;
  for(let t=0;t<=h;t++){
   const same=filt(x)===z.slice(t,z.length-t||undefined); // t=0 gives full length
   checks++;ok&&=same;
   const s=strip(z);frames.push({t,offset:z.search(/[1-8]/)-p,word:s,classification:classify(s),microMatch:same});
   if(/^4{4,}$/.test(s)){const zz=step(step(z)),m=s.length-4,expected=m?"0".repeat(z.indexOf(s)+2)+"4".repeat(m)+"0".repeat(z.length-z.indexOf(s)-2-m):"0".repeat(z.length);red&&=zz===expected;reductionChecks++}
   if(t<h){x=micro(x);z=step(z)}
  }
  const tail=frames.slice(-4).map(f=>f.classification);
  cases.push({n,h,p,raw:raw(n,p),paper:paper[n%4],candidate:candidate[n%4],paperMatch:tail.every(c=>c===paper[n%4]),candidateMatch:tail.every(c=>c===candidate[n%4]),allMicroMatch:ok,reductionMatch:red,frames})
 }
 return {version:"reference-preflight-v1",scope:"n=1..64; deterministic engineered infinite-domain finite cones; no seeds",checks,reductionChecks,summary:{cases:cases.length,rawMatches:cases.filter(c=>c.allMicroMatch).length,paperMatchesLong:cases.filter(c=>c.n>=4&&c.paperMatch).length,longCases:cases.filter(c=>c.n>=4).length,candidateMatches:cases.filter(c=>c.candidateMatch).length,reductionMatches:cases.filter(c=>c.reductionMatch).length},cases}
}
console.log(JSON.stringify(run(),null,2));
