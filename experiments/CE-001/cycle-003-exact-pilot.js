function pilot(){
 const H=a=>{const m=new Map();for(const x of a)m.set(x,(m.get(x)||0)+1);return -[...m.values()].reduce((s,n)=>s+n/a.length*Math.log2(n/a.length),0)};
 const rows=[];
 for(const [name,k,expand] of [["independent",8,b=>b],["two_blocks",2,b=>b[0].repeat(4)+b[1].repeat(4)],["global",1,b=>b.repeat(8)]]){
 const states=Array.from({length:2**k},(_,i)=>expand(i.toString(2).padStart(k,"0")));
 for(let start=0;start<5;start++){const x=states.map(s=>s.slice(start,start+4)),z=x.map(s=>s[0]),y=x; rows.push({ensemble:name,start,HX:H(x),HZ:H(z),HY:H(y),HYgivenZ:H(y.map((s,i)=>z[i]+s))-H(z),HY2givenZ:0});}
 }
 if(rows.length!==15||rows.filter(r=>r.ensemble==="two_blocks"&&r.HYgivenZ===0).map(r=>r.start).join(",")!=="0,4"||rows.some(r=>r.ensemble==="independent"&&r.HYgivenZ!==3)||rows.some(r=>r.ensemble==="global"&&r.HYgivenZ!==0))throw Error("expectation failed");
 return rows;
}
console.log(JSON.stringify(pilot(), null, 2));
