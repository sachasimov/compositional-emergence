function run(){
 const N=15, empty=()=>Array(N*N).fill(0), put=(a,r,c)=>{a[((r+N)%N)*N+(c+N)%N]=1}, step=a=>a.map((v,i)=>{let r=Math.floor(i/N),c=i%N,n=0;for(let dr=-1;dr<=1;dr++)for(let dc=-1;dc<=1;dc++)if(dr||dc)n+=a[((r+dr+N)%N)*N+(c+dc+N)%N];return +(n===3||(v===1&&n===2))}), evolve=(a,t)=>{for(let i=0;i<t;i++)a=step(a);return a}, union=(a,b)=>a.map((v,i)=>v|b[i]), blink=(r,c,p)=>{let a=empty();for(let k=-1;k<=1;k++)put(a,r+(p?k:0),c+(p?0:k));return a}, mask=(a,r,c)=>{let s=[];for(let dr=-1;dr<=1;dr++)for(let dc=-1;dc<=1;dc++)s.push(a[(r+dr)*N+c+dc]);return s.join("")}, H=a=>{let m=new Map();for(let x of a)m.set(x,(m.get(x)||0)+1);return -[...m.values()].reduce((s,n)=>s+n/a.length*Math.log2(n/a.length),0)}, joint=(a,b)=>a.map((v,i)=>v+"|"+b[i]), cond=(a,b)=>H(joint(a,b))-H(b), occ=x=>[...x].reduce((s,v)=>s+Number(v),0), counts=x=>{let r=[0,0,0],c=[0,0,0];for(let i=0;i<9;i++){r[Math.floor(i/3)]+=Number(x[i]);c[i%3]+=Number(x[i])}return r.join("")+c.join("")};
 const b=blink(5,7,0);if(evolve(b,2).join("")!==b.join(""))throw Error("blinker");
 let g=empty(),gs=empty();for(let [r,c] of [[0,1],[1,2],[2,0],[2,1],[2,2]]){put(g,r+5,c+5);put(gs,r+6,c+6)}for(let p=0;p<4;p++)if(evolve(g,p+4).join("")!==evolve(gs,p).join(""))throw Error("glider");
 const rows=[], coupling=[];
 for(let d of [3,4,5,6])for(let t of [1,2,4]){
 const cases=[];for(let p of [0,1])for(let q of [0,1]){let a=blink(5,7,p),b=blink(5+d,7,q),x=union(a,b),y=evolve(x,t),iso=union(evolve(a,t),evolve(b,t));cases.push({p,q,xa:mask(x,5,7),xb:mask(x,5+d,7),ya:mask(y,5,7),yb:mask(y,5+d,7),different:y.join("")!==iso.join("")})}
 let ya=cases.map(c=>c.ya),yb=cases.map(c=>c.yb);coupling.push({d,t,MI:H(ya)+H(yb)-H(joint(ya,yb)),different:cases.filter(c=>c.different).length,cases});
 for(let region of ["a","b","union"]){let X=cases.map(c=>region==="union"?c.xa+c.xb:c["x"+region]),Y=cases.map(c=>region==="union"?c.ya+c.yb:c["y"+region]),Z=X.map(occ),Q=X.map(x=>region==="union"?counts(x.slice(0,9))+counts(x.slice(9)):counts(x));rows.push({d,t,region,HX:H(X),HZ:H(Z),HQ:H(Q),HY:H(Y),HYgivenZ:cond(Y,Z),HYgivenQ:cond(Y,Q),HYgivenX:cond(Y,X)})}
 }
 if(rows.length!==36||coupling.length!==12||coupling.some(c=>c.d===6&&(c.MI!==0||c.different!==0))||rows.some(r=>r.d===6&&r.region!=="union"&&(r.HYgivenZ!==1||r.HYgivenQ!==0)))throw Error("expectation");
 return {rows,coupling,assertions:"passed"};
}
console.log(JSON.stringify(run(),null,2));
