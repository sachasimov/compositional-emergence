function reference(){
const F="ABDFIM".split("");
const R=[["AB","C","M"],["AD","E","O"],["CF","G","A"],["BE","H","N"],["CI","L","P"],["CM","N","E"],["DM","O","H"],["FL","P","D"]].map(([a,p,c],i)=>({id:i+1,a:a.split(""),p,c}));
const closure=(f,r)=>{const s=new Set(f);let old;do{old=s.size;for(const t of r)if(t.a.every(x=>s.has(x)))s.add(t.p)}while(s.size!==old);return s};
const enabled=(t,s)=>t.a.every(x=>s.has(x))&&s.has(t.c);
function enumerate(f,r){const rows=[];for(let m=0;m<2**r.length;m++){const sub=r.filter((_,i)=>m&(1<<i)),s=closure(f,sub),raf=sub.length>0&&sub.every(t=>enabled(t,s)),closed=raf&&r.every(t=>!enabled(t,s)||sub.includes(t));rows.push({mask:m,raf,closed})}return rows}
const rows=enumerate(F,R);
const ids=(m,r)=>r.filter((_,i)=>m&(1<<i)).map(t=>t.id);
const raf=rows.filter(x=>x.raf).map(x=>ids(x.mask,R));const closed=rows.filter(x=>x.closed).map(x=>ids(x.mask,R));
const construct=new Set(F);const caf=[];let change;do{change=false;for(const t of R)if(!caf.includes(t.id)&&enabled(t,construct)){caf.push(t.id);construct.add(t.p);change=true}}while(change);
const pair=[1,2].flatMap(k=>R.map(t=>{const rename=s=>F.includes(s)?s:s+k;return{id:`${k}.${t.id}`,a:t.a.map(rename),p:rename(t.p),c:rename(t.c)}}));
const pairRows=enumerate(F,pair);
const pairs={subsets:pairRows.length,raf:pairRows.filter(x=>x.raf).length,closed:pairRows.filter(x=>x.closed).length};
const rejectedPrediction=(closed.length+1)**2-1;
const predicted={raf:(raf.length+1)**2-1,closed:closed.length**2};
if(pairs.raf!==predicted.raf||pairs.closed!==predicted.closed||rejectedPrediction===pairs.closed)throw Error("factorization");
const states=[{B:1,E1:1,E2:0,N1:1,N2:0},{B:1,E1:1,E2:0,N1:0,N2:1}];
const rate=states.map(s=>({aggregate:{B:s.B,E:s.E1+s.E2,N:s.N1+s.N2},catalytic:s.B*(s.E1*s.N1+s.E2*s.N2),spontaneous:s.B*(s.E1+s.E2)}));
if(rate[0].catalytic===rate[1].catalytic)throw Error("witness");
return {food:F,reactions:R,subsets:rows.length,raf,closed,caf,pairs,predicted,rejectedPrediction,states,rate,metric:{alwaysAllPresent:8/2,halfTimeOneMissing:0.5+7.5/101},rows,pairRafMasks:pairRows.filter(x=>x.raf).map(x=>x.mask),pairClosedMasks:pairRows.filter(x=>x.closed).map(x=>x.mask)}
}
console.log(JSON.stringify(reference(),null,2));
