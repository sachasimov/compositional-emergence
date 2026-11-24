// Rule54 reference preflight; Hanson & Crutchfield, Physica D 103 (1997), Fig.8 and Table 1.
function run(){
const D={"0011":"1","0101":"2","1001":"3","0000":"4","1100":"5","1010":"6","0110":"7","1111":"8"};
const lab=w=>D[w]||"0", phi=w=>String((54>>parseInt(w,2))&1);
const table={};for(let k=0;k<64;k++){let x=k.toString(2).padStart(6,"0"),z=[0,1,2].map(i=>lab(x.slice(i,i+4))).join(""),y=[0,1,2,3].map(i=>phi(x.slice(i,i+3))).join("");if(z in table&&table[z]!==lab(y))throw Error("closure");table[z]=lab(y)}
const cat={A:["444","50401","3","888"],B:["44","5001","26","88"],R:["5","2"],L:["1","6"]};
const specs=Object.entries(cat).flatMap(([type,ws])=>ws.map((word,phase)=>({type,phase,word})));
const at=(s,i)=>s[i]||"0";
const decode=z=>{let i=z.search(/[1-8]/);if(i<0)return null;let rev=Object.fromEntries(Object.entries(D).map(([w,l])=>[l,w])),w=rev[z[i]],s=Array(z.length+3);for(let j=0;j<4;j++)s[i+j]=w[j];for(let j=i+1;j<z.length;j++){let pre=s.slice(j,j+3).join("");let v=z[j]==="0"?String(1^+pre[0]^+pre[1]^+pre[2]):rev[z[j]][3];if(lab(pre+v)!==z[j])return null;s[j+3]=v}for(let j=i-1;j>=0;j--){let post=s.slice(j+1,j+4).join("");let v=z[j]==="0"?String(1^+post[0]^+post[1]^+post[2]):rev[z[j]][0];if(lab(v+post)!==z[j])return null;s[j]=v}return s.join("")};
let directChecks=0;
const evolve=s=>{let n=Array.from(s,(_,i)=>{let v=table[at(s,i-1)+s[i]+at(s,i+1)];if(v===undefined)throw Error("invalid triple "+s+" "+i);return v}).join("");
if(/[1-8]/.test(s)){let raw=decode(s);if(!raw)throw Error("inconsistent typed state");let x=Array.from({length:raw.length-2},(_,i)=>phi(raw.slice(i,i+3))).join("");let y=Array.from({length:x.length-3},(_,i)=>lab(x.slice(i,i+4))).join("");if(y!==n.slice(1,-1))throw Error("raw correspondence");directChecks++}
return n};
function parse(z){let cand=[];for(let i=0;i<z.length;i++)for(let p of specs){if(at(z,i-1)==="0"&&z.slice(i,i+p.word.length)===p.word&&at(z,i+p.word.length)==="0")cand.push({...p,start:i,end:i+p.word.length})}
cand.sort((a,b)=>b.word.length-a.word.length||a.start-b.start);let kept=[],overlap=[];for(let c of cand){if(kept.some(k=>c.start<k.end&&k.start<c.end))overlap.push(c);else kept.push(c)}kept.sort((a,b)=>a.start-b.start);let out=z.split("");for(let p of kept)for(let i=p.start;i<p.end;i++)if(z[i]!=="0")out[i]=p.type;return{tokens:kept,overlap,unrecognized:out.filter(c=>/[1-8]/.test(c)).length,output:out.join("")}}
const phases=specs.map(p=>{let z="0".repeat(8)+p.word+"0".repeat(8);let raw=decode(z),next=evolve(z),q=parse(next),n=q.tokens[0];return{...p,z,raw,next,tokens:q.tokens,overlap:q.overlap,ok:!!raw&&q.unrecognized===0&&q.tokens.length===1&&n.type===p.type&&n.phase===(p.phase+1)%cat[p.type].length,shift:n?.start-8}});
const pairs=[["A","L","LARR"],["R","A","LLAR"],["B","L","R"],["R","B","L"],["R","L","B"]];
let outcomes=[],rejected=[],unknown=new Set();
for(const [a,b,expect] of pairs)for(const p of specs.filter(x=>x.type===a))for(const q of specs.filter(x=>x.type===b))for(let gap=8;gap<=11;gap++){
 let z="0".repeat(48)+p.word+"0".repeat(gap)+q.word+"0".repeat(48),raw=decode(z);
 let id={a,b,pa:p.phase,pb:q.phase,gap,expect};
 if(!raw){rejected.push(id);continue}
 let frames=[];
 for(let t=0;t<=36;t++){let r=parse(z),types=r.tokens.map(p=>p.type).join("");frames.push({t,z:z.replace(/^0+|0+$/g,""),offset:z.search(/[1-8]/),types,u:r.unrecognized,overlap:r.overlap.length});
 if(r.unrecognized)for(let m of r.output.matchAll(/[1-8]+/g))unknown.add(m[0]);
 if(t<36)z=evolve(z);
 }
 let initial=frames[0].types===a+b&&frames[0].u===0,pass=initial&&frames.slice(-4).every(f=>f.types===expect&&f.u===0);
 outcomes.push({...id,raw,initial,pass,frames});
}
const phaseLoss=phases.filter(p=>(p.type==="A"||p.type==="B")&&(p.phase===0||p.phase===3)).map(p=>({type:p.type,phase:p.phase,z:p.z,macro:parse(p.z).output,nextMacro:parse(p.next).output}));
return {cat,phases,invalidTranscription:{word:"501",compatible:!!decode("0000000050100000000"),reason:"first draft omitted one zero in beta phase 1, failed local typed validity"},directChecks,pairCounts:pairs.map(([a,b,expect])=>({a,b,expect,valid:outcomes.filter(x=>x.a===a&&x.b===b).length,pass:outcomes.filter(x=>x.a===a&&x.b===b&&x.pass).length,rejected:rejected.filter(x=>x.a===a&&x.b===b).length})),unknown:[...unknown].sort(),phaseLoss,outcomes,rejected};
}
console.log(JSON.stringify(run(),null,2));
