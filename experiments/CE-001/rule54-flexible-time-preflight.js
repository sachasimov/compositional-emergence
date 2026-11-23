// Reference-method preflight, not a confirmatory simulation. See report for limitations.
function audit(){
  const ex={M:["1","-","0","o"],P:["1","0","+","o"]};
  function parse(s){
    let t=0,x=0;const cells=new Map();
    function put(t,x,b){const k=t+","+x;if(cells.has(k)&&cells.get(k)!==b)throw Error("conflict "+k);cells.set(k,b)}
    for(const a of s)for(const z of ex[a]||[a]){
      if(z==="+"||z==="-"){t+=z==="+"?1:-1;x--}
      else if(z==="o"){put(t,x,1)}
      else if(z==="0"||z==="1"){put(t,x,Number(z));x++}
      else throw Error("unknown token "+z)
    }
    return {cells,end:[t,x]}
  }
  const rule=(l,c,r)=>(54>>(4*l+2*c+r))&1;
  function check(id,a,b,group){
    try{
      const A=parse(a),B=parse(b),all=new Map();
      const coords=[...A.cells.keys(),...B.cells.keys()].map(k=>k.split(",").map(Number));
      const tmin=Math.min(...coords.map(v=>v[0])),tmax=Math.max(...coords.map(v=>v[0]));
      const xmin=Math.min(...coords.map(v=>v[1]))-(tmax-tmin)-1,xmax=Math.max(...coords.map(v=>v[1]))+(tmax-tmin)+1;
      for(let t=tmin;t<=tmax;t++)for(let x=xmin;x<=xmax;x++){
        const k=t+","+x;let predicted;
        if(t>tmin){const v=[-1,0,1].map(d=>all.has((t-1)+","+(x+d))?[all.get((t-1)+","+(x+d))]:[0,1]);const poss=new Set();for(const l of v[0])for(const c of v[1])for(const r of v[2])poss.add(rule(l,c,r));if(poss.size===1)predicted=[...poss][0]}
        if(A.cells.has(k)){if(predicted!==undefined&&predicted!==A.cells.get(k))throw Error("inconsistent input "+k);all.set(k,A.cells.get(k))}
        else if(predicted!==undefined)all.set(k,predicted)
      }
      const mismatch=[...B.cells].filter(([k,v])=>all.get(k)!==v).map(([k,v])=>({k,expected:v,actual:all.get(k)??null}));
      const sameEnd=A.end.join()===B.end.join();
      return {id,group,a,b,endA:A.end,endB:B.end,mismatch,pass:sameEnd&&!mismatch.length}
    }catch(e){return {id,group,a,b,pass:false,error:String(e)}}
  }
  const m="MM",p="PP",R="M11o",L="11P",O="PM",E="P1M";
  const cases=[
    ["26","1000o",p+m],["27",m+p,"1000o"],["29a",m+p,p+m],["31a","MP","11o"],
    ["36a",R+p,p+R],["36a-reflected",m+L,L+m],
    ["36b",m+O+p,p+O+m],["36c",m+E+p,p+E+m],
    ["37",R+L,p+O+m],
    ["39a",R+O+p,p+R+m],["39b",R+O+L,p+p+m+m],
    ["40a",R+O,p+"M"+m],["40b-1","M"+p,R],["40b-2","M"+L,p+m],
    ["41a",R+E,p+m+"1M"],["41b-1","1M"+p,"1"+L],["41b-2","1M"+L,"1"+p+m],
    ["41c-1",m+"1"+p,"11111o"],["41c-2",m+"1"+L,L+"1"+m],["41c-3",R+"1"+L,p+E+m],
    ["41d-1",m+"11111o"+p,L+E+R],["41d-2",m+"11111o"+L,L+p+p+"1"+m+m],["41d-3",R+"11111o"+L,p+p+E+m+m]
  ];
  for(let k=0;k<=8;k++){
    if(k>0)cases.push(["35a-k"+k,"M"+"1".repeat(2*k)+"P","P".repeat(k+1)+"M".repeat(k+1)]);
    cases.push(["35b-k"+k,"M"+"1".repeat(2*k+1)+"P","P".repeat(k+1)+"1"+"M".repeat(k+1)])
  }
  const extras=[
    ["39a-alt",R+O+p,p+L+m,"candidate-correction"],
    ["40b-1-alt","M"+p,L,"candidate-correction"],
    ["41d-2-alt",m+"11111o"+L,L+p+"1"+m+m,"candidate-correction"],
    ["41b-1-initial-transcription","1M"+p,"1"+R,"transcription-error"],
    ["negative-control","1000o","0000o","negative-control"]
  ];
  return [...cases.map(c=>check(...c,"reference")),...extras.map(c=>check(...c))];
}
console.log(JSON.stringify(audit(), null, 2));
