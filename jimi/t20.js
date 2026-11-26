const {chromium}=require('playwright');const out=process.argv[2];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:900}});
await p.route('http://app.test/**',r=>{const f=new URL(r.request().url()).pathname.slice(1);r.fulfill({path:require('path').join(__dirname,'..',f)})});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('dialog',d=>d.accept());
await p.goto('http://app.test/index.html');await p.waitForSelector('.sec');
await p.click('.sec >> nth=0');const bks=await p.$$eval('.bk',e=>e.map(x=>x.innerText.replace(/\n/g,' ')));const bi=bks.findIndex(x=>new RegExp(process.argv[5]).test(x));console.log(bks,bi);await p.click('.bk >> nth='+bi);await p.waitForSelector('.item');
console.log((await p.$$eval('.item',e=>e.slice(1,3).map(x=>x.innerText.replace(/\n/g,' | ')))).join('\n'));
let broken=0;
for(let ti=+process.argv[3];ti<+process.argv[4];ti++){
  await p.click('.item >> nth='+ti);await p.waitForSelector('.tset');
  await p.click('.ticks span >> nth=0');await p.click('text=Boshlash');
  const n=await p.evaluate(()=>S.qs.length);
  for(let i=0;i<n;i++){
    await p.waitForSelector('.opt');
    const im=await p.$('.qimg');if(im&&!globalThis.shot&&(await im.getAttribute('src')).includes('map')){globalThis.shot=1;await p.waitForTimeout(300);await p.screenshot({path:out+'/map.png',fullPage:true})}if(im){await p.waitForTimeout(120);if(!(await im.evaluate(x=>x.complete&&x.naturalWidth>0)))broken++}
    // birinchi mavzuda hammasi to'g'ri, ikkinchisida faqat juft savollar to'g'ri, qolganlarida birinchi variant
    const k=await p.evaluate(([ti,i])=>{const o=S.qs[S.i].o;const c=o.findIndex(x=>x.ok);if(ti===1)return c;if(ti===2)return i%2===0?c:o.findIndex(x=>!x.ok);return 0},[ti,i]);
    await p.click('.opt >> nth='+k);await p.click('.note + .btn');
  }
  await p.waitForSelector('.score');
  if(ti<3){console.log('topic',ti+1,n,'q:',await p.$eval('.score',e=>e.innerText.replace(/\n/g,' | ')));await p.screenshot({path:out+'/score'+ti+'.png'})}
  await p.click('text=Mavzular');await p.waitForSelector('.item');
}
console.log('broken imgs',broken,'errs',errs);await b.close()})();
