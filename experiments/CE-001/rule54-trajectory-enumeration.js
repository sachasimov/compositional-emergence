// Same-author cross-check of finite-cone SAT via explicit earliest-row enumeration.
function exhaustive(fixtures){
  // Independent algorithm within same author session: directly enumerate earliest row completions.
  function decode(s){
    const out=[];let x=0,t=0;
    for(const token of s.replaceAll("M","1-0o").replaceAll("P","10+o")){
      if(token==="-"){x--;t--;continue}
      if(token==="+"){x--;t++;continue}
      out.push([t,x,token==="0"?0:1]);if(token!=="o")x++;
    }
    return out;
  }
  const results=[];
  for(const f of fixtures){
    const a=decode(f.a),b=decode(f.b),w=f.input.witness;
    if(!w){results.push({id:f.id,status:"no input witness"});continue}
    const {t0,x0}=w,n=w.bits.length;
    const row=Array(n).fill(-1);
    for(const [t,x,v] of a)if(t===t0)row[x-x0]=v;
    const unknown=row.map((x,i)=>x===-1?i:-1).filter(x=>x>=0);
    if(unknown.length>16){results.push({id:f.id,status:"skipped >16 unknown bits",unknown:unknown.length});continue}
    const maxT=Math.max(...a.concat(b).map(v=>v[0]));
    let compatible=0,joint=0,counter=0;
    for(let mask=0;mask<2**unknown.length;mask++){
      const q=row.slice();unknown.forEach((idx,j)=>q[idx]=(mask>>j)&1);
      let p=q,lo=x0,okA=true,okB=true;
      for(let t=t0;t<=maxT;t++){
        for(const [tt,x,v] of a)if(tt===t&&p[x-lo]!==v)okA=false;
        if(!okA)break;
        for(const [tt,x,v] of b)if(tt===t&&p[x-lo]!==v)okB=false;
        const next=[];for(let i=1;i<p.length-1;i++)next.push((54>>(4*p[i-1]+2*p[i]+p[i+1]))&1);p=next;lo++;
      }
      if(okA){compatible++;if(okB)joint++;else counter++}
    }
    const match=(compatible>0)===(f.input.status==="sat")&&(joint>0)===(f.joint.status==="sat")&&(counter>0)===(f.counter.status==="sat");
    results.push({id:f.id,status:"enumerated",unknown:unknown.length,completions:2**unknown.length,compatible,joint,counter,match});
  }
  return results;
}
const fs=require('node:fs');
const input=JSON.parse(fs.readFileSync(process.argv[2]||'results/CE-001/rule54-trajectory-consistency.json','utf8'));
console.log(JSON.stringify(exhaustive(input.results),null,2));
