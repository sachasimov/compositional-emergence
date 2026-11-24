// Same-author finite trajectory consistency check; not independent audit.
function run(fixtures){
  // Exact global trajectory constraints over finite backwards cones, separate from Flexible Time closure.
  const step=(l,c,r)=>Number(Boolean((l||c||r)&&!(l&&c)&&!(c&&r)));
  function decode(s){
    let t=0,x=0;const events=new Map();
    const expanded=s.replace(/M/g,"1-0o").replace(/P/g,"10+o");
    for(const a of expanded){
      if(a==="+"||a==="-"){t+=a==="+"?1:-1;x--;continue}
      if(!"01o".includes(a))throw Error("unknown "+a);
      const k=t+","+x,b=a==="0"?0:1;
      if(events.has(k)&&events.get(k)!==b)throw Error("contradictory event");
      events.set(k,b);if(a!=="o")x++;
    }
    return {events,end:[t,x]};
  }
  function solve(clauses,n,cap=10000){
    let nodes=0;
    function rec(a){
      if(++nodes>cap) return "limit";
      let changed=true;
      while(changed){
        changed=false;
        for(const clause of clauses){
          let free=0,last=0,sat=false;
          for(const l of clause){const v=a[Math.abs(l)];if(v===-1){free++;last=l}else if(v===Number(l>0)){sat=true;break}}
          if(sat)continue;if(!free)return null;
          if(free===1){a[Math.abs(last)]=Number(last>0);changed=true}
        }
      }
      let best=null;
      for(const clause of clauses){
        if(clause.some(l=>a[Math.abs(l)]===Number(l>0)))continue;
        const free=clause.filter(l=>a[Math.abs(l)]===-1);
        if(!best||free.length<best.length)best=free;
      }
      if(!best){for(let i=1;i<=n;i++)if(a[i]===-1)a[i]=0;return a}
      const v=Math.abs(best[0]);
      for(const b of [0,1]){const q=a.slice();q[v]=b;const ret=rec(q);if(ret!==null)return ret}
      return null;
    }
    const a=new Int8Array(n+1).fill(-1),v=rec(a);
    return {status:v==="limit"?"limit":v===null?"unsat":"sat",nodes,model:v instanceof Int8Array?v:null};
  }
  function one(f){
    const A=decode(f.a),B=decode(f.b),keys=[...A.events.keys(),...B.events.keys()];
    const pts=keys.map(k=>k.split(",").map(Number)),t0=Math.min(...pts.map(v=>v[0])),t1=Math.max(...pts.map(v=>v[0]));
    // Union of backward cones; no exterior boundary conditions are imposed.
    const cells=new Map();function add(t,x){const k=t+","+x;if(cells.has(k))return;cells.set(k,cells.size+1);if(t>t0)for(const d of [-1,0,1])add(t-1,x+d)}
    for(const [t,x] of pts)add(t,x);
    const id=(t,x)=>cells.get(t+","+x),clauses=[];
    for(const [k,i] of cells){const [t,x]=k.split(",").map(Number);if(t===t0)continue;
      const p=[id(t-1,x-1),id(t-1,x),id(t-1,x+1)];
      for(let bits=0;bits<8;bits++){const b=[(bits>>2)&1,(bits>>1)&1,bits&1];clauses.push([...p.map((v,j)=>b[j]?-v:v),step(...b)?i:-i])}
    }
    const literals=E=>[...E].map(([k,b])=>b?cells.get(k):-cells.get(k));
    const a=literals(A.events),b=literals(B.events);
    const base=clauses.concat(a.map(l=>[l]));
    const tests={input:solve(base,cells.size),joint:solve(base.concat(b.map(l=>[l])),cells.size),counter:solve(base.concat([b.map(l=>-l)]),cells.size)};
    function witness(s,kind){
      if(!s.model)return null;
      const xx=[...cells.keys()].map(k=>k.split(",").map(Number)).filter(v=>v[0]===t0).map(v=>v[1]);
      const lo=Math.min(...xx),hi=Math.max(...xx);
      let row=Array.from({length:hi-lo+1},(_,i)=>id(t0,lo+i)?s.model[id(t0,lo+i)]:0);
      const bits=row.join(""),vals=new Map();let x0=lo;
      for(let t=t0;t<=t1;t++){
        row.forEach((v,i)=>vals.set(t+","+(x0+i),v));
        row=row.slice(1,-1).map((_,i)=>step(row[i],row[i+1],row[i+2]));x0++;
      }
      const matches=E=>[...E].every(([k,b])=>vals.get(k)===b);
      const okA=matches(A.events),okB=matches(B.events);
      if(!okA||(kind==="joint"&&!okB)||(kind==="counter"&&okB))throw Error("invalid witness "+f.id+" "+kind);
      return {t0,x0:lo,bits,okA,okB};
    }
    const results={};for(const [k,s] of Object.entries(tests))results[k]={status:s.status,nodes:s.nodes,witness:witness(s,k)};
    return {id:f.id,group:f.group,priorPass:f.pass,a:f.a,b:f.b,variables:cells.size,clauses:clauses.length,displacementMatches:A.end.join()===B.end.join(),...results};
  }
  return fixtures.map(one);
}
const fs = require('node:fs');
const input = JSON.parse(fs.readFileSync(process.argv[2] || 'results/CE-001/rule54-flexible-time-preflight.json','utf8'));
console.log(JSON.stringify(run(input.results), null, 2));
