import re
#!/usr/bin/env python3
"""Generate the one-page site xxia99.github.io (al-folio style, half-and-half research rows). Run: python build.py"""
import os
ROOT=os.path.dirname(os.path.abspath(__file__))
# Cloudflare Web Analytics: paste the site token here; pages carry no counter while it is empty.
CF_TOKEN="4b68bf452941403d855d50c3467e19e0"
CFWA=('<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{"token": "%s"}\'></script>\n'%CF_TOKEN) if CF_TOKEN else ""

NAV=[("index.html","about"),("publications.html","publications"),("projects.html","projects"),("news.html","news"),("cv.html","cv")]
BIO1="My research combines multi-agent reinforcement learning with statistical process control. Where a mobile sensor goes decides what is observed, so I design learning-based sampling and dispatch policies that let fleets of agents, such as unmanned aerial vehicles, detect anomalies quickly in large systems while keeping false alarms under control, with guarantees on coverage, focusing, and detection delay."
BIO2='Before Madison, I was a research assistant in the <a href="https://thu-sail-lab.github.io/home/">Superintelligence and Industrial Lab (SAIL)</a> at Tsinghua University, advised by <a href="https://www.ie.tsinghua.edu.cn/eng/info/1051/1031.htm">Prof. Chen Zhang</a>, working on deep reinforcement learning for bilevel optimization in supply chain and manufacturing systems. I hold an M.Sc. in Electrical and Computer Engineering from Georgia Tech and a B.Eng. in Electrical Engineering and Automation from Tianjin University.'
INTERESTS="multi-agent reinforcement learning, sequential change detection, adaptive sampling and dispatch, statistical process control, unmanned aerial vehicles, bilevel optimization, resilient supply chains, language models for text mining"

# key, badge, title, authors, venue, status, award, summary, links, year-group, preview caption, hover label
PUBS=[
 dict(k="dispatchppo",badge="NeurIPS",title="Learning Collision-Free Dispatch Policies for Route-Wise Decision-Dependent Anomaly Detection",
      au="<b>Xin Xia</b>, Chen Zhang, and Kaibo Liu",venue="Advances in Neural Information Processing Systems (NeurIPS), 2026",status="",award="",
      abs="A dispatch policy for UAV fleets that assigns moves sequentially, one UAV at a time, so joint moves are collision-free by construction and decoded in linear time, with guarantees on coverage, focusing, and detection delay. Validated on the Robotarium and on a wildfire reconstructed from satellite frames.",
      links=[("Paper","https://openreview.net/pdf?id=s01jPERPlb"),("Code","https://github.com/xxia99/DispatchPPO"),("Poster","data/posters/NeurIPS2026_DispatchPPO_poster.pdf")],year="2026",cap="NeurIPS 2026 poster",lab="Poster",sel=True),
 dict(k="scan",badge="INFORMS",title="SCAN: Networked Multi-Agent Reinforcement Learning for Decentralized Anomaly Detection in Graph-Structured Systems",
      au="<b>Xin Xia</b> and Kaibo Liu",venue="INFORMS Annual Meeting, 2026",status="journal version in preparation",award='<b class="win">Winner</b>INFORMS QSR Best Refereed Paper Award, 2026',award_url="https://www.linkedin.com/posts/informs-quality-statistics-and-reliability-qsr_informs-quality-statistics-and-reliability-activity-7524611375281881088-RDX0",
      abs="Each drone learns from its own evidence and a few messages from neighbours, moves safely under mobility constraints, and the team raises a calibrated alarm. Demonstrated on wildfire and traffic cases with a drone fleet in a 3D simulator.",
      links=[("Demo","images/fulls/scan.jpg")],year="2026",cap="SCAN: drone fleet in the wildfire simulator (overview, chase view, HUD)",lab="Demo",sel=True),
 dict(k="hass",badge="Technometrics",title="Multi-Agent Reinforcement Learning for Anomaly Detection with Hierarchical Adaptive Sampling Strategy",
      au="<b>Xin Xia</b>, Jie Guo, Ziqian Zheng, Yujie Ma, Chen Zhang, and Kaibo Liu",venue="Technometrics",status="accepted",award="Finalist, IISE QCRE Best Track Paper Competition, 2025",award_url="https://myemail.constantcontact.com/QCRE-News---May-2025.html?aid=vKcqr1w06AU&amp;soid=1101700049774#:~:text=Interactive%20Resource%20Planning%20and%20Change%20Detection",
      abs="Limited monitoring resources are allocated across many data streams by a hierarchy of learned agents, so that the streams most likely to carry the change are observed first.",
      links=[("Figure","images/fulls/hass.png"),("Testbed","images/fulls/hass_iot.png"),("Code","https://github.com/xxia99/PAD"),("Poster","data/posters/Technometrics_PAD_poster.pdf")],year="2026",img="images/fulls/hass.png",ar=' style="aspect-ratio:1466/526"',cap="Hierarchical adaptive sampling: framework overview",lab="Figure",fig="Flat and hierarchical system structures",sel=True),
 dict(k="kappa",badge="IJDS",title="Generating Interpretable Document Portraits via Structure-Aware Foundation Models: Application to Patent Analytics",
      au="<b>Xin Xia</b>, Yujin Wang, Jun Zhou, Guisheng Zhong, Linning Cai, Kaibo Liu, and Chen Zhang",venue="INFORMS Journal on Data Science",status="major revision",award="",
      abs="Patents are summarised into keyphrase portraits generated by a pretrained language model, which then support retrieval, clustering, and trend analysis.",
      links=[("Code","https://github.com/xxia99/SetPLM"),("Model","images/fulls/kappa_model.png")],year="2026",cap="KAPPA: portrait generation and portrait-based analytics",lab="Figure",img="images/fulls/kappa.png",ar=' style="aspect-ratio:835/335"',fig="Framework overview"),
 dict(k="bsac",badge="IEEE TEM",title="A Deep Reinforcement Learning Method Solving Bilevel Optimization for Product Design Considering Remanufacturing",
      au="Yujie Ma, <b>Xin Xia</b>, Jie Guo, and Chen Zhang",venue="IEEE Transactions on Engineering Management, 72, 573-590, 2025",status="",award="",
      abs="Product design as the leader and remanufacturing as the follower in a Stackelberg game, solved by a bilevel SAC algorithm (BSAC) with convergence and optimality guarantees.",
      links=[("DOI","https://doi.org/10.1109/TEM.2025.3535771"),("Poster","data/posters/INFORMS2025_QSR_BSAC_poster.pdf")],year="2025",pdf="data/posters/INFORMS2025_QSR_BSAC_poster.pdf",cap="Poster: solving bilevel optimization with deep reinforcement learning (INFORMS QSR 2025)",lab="Poster",fig="Poster, 2025 INFORMS Annual Meeting"),
 dict(k="ijpe",badge="IJPE",title="Bilevel Joint Optimization for Product Design Changes with a Resilient Supply Chain Based on Deep Reinforcement Learning",
      au="Yujie Ma, <b>Xin Xia</b>, Peiyao Liu, and Chen Zhang",venue="International Journal of Production Economics, 290, 109791, 2025",status="",award="",
      abs="Design changes and the supply chain that must absorb them are optimised together under disruption risk.",
      links=[("DOI","https://doi.org/10.1016/j.ijpe.2025.109791")],year="2025",cap="Policy and value networks of the adapted SAC for the bilevel joint optimization model",lab="Figure",img="images/fulls/ijpe.png",ar=' style="aspect-ratio:2028/595"',fig="Policy and value networks of the adapted SAC"),
 dict(k="msom",badge="M&amp;SOM",title="Strengthening Supply Chain Resilience Through Coordinating Optimization of Product Design and Inventory Management: A Multi-Agent Deep Reinforcement Learning Approach",
      au="Yujie Ma, <b>Xin Xia</b>, Chen Zhang, and Nan Chen",venue="Manufacturing &amp; Service Operations Management",status="submitted",award="",
      abs="A multi-agent deep reinforcement learning approach in which each echelon learns to cooperate with its upstream and downstream neighbours.",links=[],year="Under review",cap="A bilevel supply chain system: platform as leader, supply chain members as followers",lab="Figure",img="images/fulls/msom.png",ar=' style="aspect-ratio:296/158"',fig="Bilevel supply chain system"),
 dict(k="iise",badge="IISE Trans.",title="Quality-Driven Multi-Agent Coordination in Multi-Stage Manufacturing Systems: A Distributionally Robust Bilevel Optimization Framework with Reinforcement Learning",
      au="Yujie Ma, Jie Guo, <b>Xin Xia</b>, and Chen Zhang",venue="IISE Transactions",status="under review",award="",
      abs="A distributionally robust bilevel optimization framework with reinforcement learning for coordinating quality decisions across manufacturing stages.",links=[],year="Under review",cap="",lab=""),
 dict(k="causal",badge="arXiv",title="Multi-Agent Causal Discovery Using Large Language Models",
      au="Hao Duong Le, <b>Xin Xia</b>, Haijie Xu, and Chen Zhang",venue="arXiv:2407.15073, 2024",status="",award="",
      abs="Several LLM agents with different roles debate and vote on causal edges, combining metadata with observational data.",
      links=[("arXiv","https://arxiv.org/abs/2407.15073")],year="2024",cap="arXiv:2407.15073, first page",lab="Preprint",fig="Preprint, arXiv:2407.15073"),
]
PATENTS=[("CN115205869A","P. Liu, <b>X. Xia</b>, Z. Yan, Y. Liu, J. Xiao.",'<a href="https://patents.google.com/patent/CN115205869A/en">Method and device for generating structured document information, electronic equipment and storage medium</a>'),
         ("CN114661545A","P. Liu, L. Huang, X. Yu, <b>X. Xia</b>, Y. Liu, J. Xiao.",'<a href="https://patents.google.com/patent/CN114661545A/en">Method, device and equipment for monitoring processor resources and storage medium</a>')]
NEWS=[('Nov 2026','Honored that <a class="nt" href="project-fleets.html#proj-scan"><em>SCAN: Networked Multi-Agent Reinforcement Learning for Decentralized Anomaly Detection in Graph-Structured Systems</em></a> won the <a class="hot" href="https://www.linkedin.com/posts/informs-quality-statistics-and-reliability-qsr_informs-quality-statistics-and-reliability-activity-7524611375281881088-RDX0" target="_blank" rel="noopener">INFORMS QSR Best Refereed Paper Award</a> at the 2026 INFORMS Annual Meeting in San Francisco!'),
      ('Nov 2026','Enjoyed giving an <a href="talks.html">invited talk</a> on <a class="nt" href="project-fleets.html#proj-dispatchppo"><em>Learning Collision-Free Dispatch Policies for Route-Wise Decision-Dependent Anomaly Detection</em></a> at the 2026 INFORMS Annual Meeting in San Francisco.'),
      ('Nov 2026','Happy to share that <a class="nt" href="project-multi-agent.html#proj-hass"><em>Multi-Agent Reinforcement Learning for Anomaly Detection with Hierarchical Adaptive Sampling Strategy</em></a> has been accepted by <em>Technometrics</em>.'),
      ('Sep 2026','Excited that <a class="nt" href="project-fleets.html#proj-dispatchppo"><em>Learning Collision-Free Dispatch Policies for Route-Wise Decision-Dependent Anomaly Detection</em></a> has been accepted at NeurIPS 2026!'),
      ('Oct 2025','Had a great time giving an <a href="talks.html">invited talk</a>, <em>Interactive Resource Allocation and Anomaly Detection via Multi-Agent Reinforcement Learning</em>, at the 2025 INFORMS Annual Meeting in Atlanta.'),
      ('Sep 2025','Our paper <a class="nt" href="project-supply-chain.html#proj-ijpe"><em>Bilevel Joint Optimization for Product Design Changes with a Resilient Supply Chain Based on Deep Reinforcement Learning</em></a> is now published in <em>International Journal of Production Economics</em>.'),
      ('May 2025','Glad that <em>Interactive Resource Planning and Change Detection via Multi-agent Reinforcement Learning</em> was selected as a <a class="hot" href="https://myemail.constantcontact.com/QCRE-News---May-2025.html?aid=vKcqr1w06AU&amp;soid=1101700049774#:~:text=Interactive%20Resource%20Planning%20and%20Change%20Detection" target="_blank" rel="noopener">finalist of the IISE QCRE Best Track Paper Competition</a> at the 2025 IISE Annual Conference in Atlanta.'),
      ('Jan 2025','Thrilled to start my Ph.D. at the University of Wisconsin-Madison with Prof. Kaibo Liu!'),
      ('Jan 2025','Our paper <a class="nt" href="project-supply-chain.html#proj-bsac"><em>A Deep Reinforcement Learning Method Solving Bilevel Optimization for Product Design Considering Remanufacturing</em></a> is out in <em>IEEE Transactions on Engineering Management</em>.'),
      ('Jul 2024','Our preprint <a class="nt" href="project-language-models.html#proj-causal"><em>Multi-Agent Causal Discovery Using Large Language Models</em></a> is now on arXiv.')]
PROJECTS=[("setplm","SetPLM","https://github.com/xxia99/SetPLM","Keyphrase generation with a pretrained language model: T5 inside the One2Set paradigm, keyword-code control and keyword-based padding. State of the art on KP20K, Inspec, Krapivin, NUS, and SemEval.","Tsinghua University, 2023"),
          ("berthrl","BerthRL","https://github.com/xxia99/bqc_scheduling","Dynamic berth and quay-crane scheduling as a bilevel problem, solved by a PPO-based algorithm that outperforms genetic algorithms, particle swarm optimization, and FIFO rules.","Georgia Tech, 2022"),
          ("dcgan","Scenario generation for integrated energy systems","https://github.com/xxia99/DCGAN-for-Scenario-Generation","A Wasserstein DCGAN learns the joint behaviour of wind, photovoltaic, heating, and power subsystems; K-means picks typical scenarios for planning.","Tianjin University, 2020")]
CV=[("2025 - present","University of Wisconsin-Madison","Ph.D. in Industrial Engineering. Advisor: Prof. Kaibo Liu."),
    ("2022 - 2025","Tsinghua University, Superintelligence and Industrial Lab (SAIL)","Research assistant, advised by Prof. Chen Zhang. Multi-agent reinforcement learning for resilient supply chains; deep reinforcement learning for bilevel optimization; keyphrase generation with pretrained language models. Co-wrote chapters on machine learning, reinforcement learning, and Monte Carlo tree search for <em>Machine Learning: Industrial Big-Data Analysis</em> (Tsinghua University Press)."),
    ("2020 - 2022","Georgia Institute of Technology","M.Sc. in Electrical and Computer Engineering."),
    ("2021 - 2022","Ping An Technology, Shenzhen","AI researcher intern. Multimodal document understanding with pretrained language models; two invention patents."),
    ("2016 - 2020","Tianjin University","B.Eng. in Electrical Engineering and Automation.")]


import subprocess
from PIL import Image as _Im

# ---------------------------------------------------------------- demos
def _hd(v):
    h=v[:-4]+"_hd.mp4"
    return h if os.path.exists(os.path.join(ROOT,h)) else v
def V(video,full,cap,fig):
    """a looping clip; `full` is the still shown if the video cannot play"""
    return dict(video="images/video/%s.mp4"%video,poster="images/video/%s_poster.jpg"%video,full=full,cap=cap,fig=fig)
def I(image,w,h,cap,fig):
    return dict(image="images/fulls/%s"%image,w=w,h=h,cap=cap,fig=fig)
def L(text,url): return '<a href="%s" target="_blank" rel="noopener">%s</a>'%(url,text)
def _size(m):
    if "w" in m: return m["w"],m["h"]
    o=subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0",os.path.join(ROOT,m["video"])],capture_output=True,text=True).stdout.strip().split(",")
    m["w"],m["h"]=int(o[0]),int(o[1]); return m["w"],m["h"]

# First entry = the demo shown on the main page; all entries appear on the projects page.
DEMOS={
 "dispatchppo":[V("robotarium_demo","images/fulls/dispatchppo_robotarium.jpg","Robotarium experiment: ten robots dispatched on the arena, with their trajectories and the detection statistic","Robot experiment (%s)"%L("Robotarium","https://www.robotarium.gatech.edu")),
                V("dispatch_demo","images/fulls/dispatchppo_ue.jpg","Five UAVs patrolling a forest in the Unreal Engine simulator; blue frustums are the camera footprints","Wildfire simulation (%s)"%L("Unreal Engine","https://www.unrealengine.com"))],
 "scan":[V("scan_demo","images/fulls/scan.jpg","SCAN: drone fleet in the wildfire simulator (overview, chase view, HUD)",
           'Scene rebuilt from satellite records (%s)<sup><a href="https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01501/html" target="_blank" rel="noopener" title="GOES-17 ABI L1b radiances (NOAA NCEI)">1</a>,<a href="https://goes.noaa.gov/documents/QuickGuide_Fire_Temperature_RGB.pdf" target="_blank" rel="noopener" title="Fire Temperature RGB recipe (NASA SPoRT)">2</a></sup>'%L("CIMSS Satellite","https://cimss.ssec.wisc.edu/satellite-blog/archives/40926")),
         V("scan_traffic","images/fulls/scan_traffic.jpg","SCAN on the Los Angeles road network: drones detect a traffic incident","LA traffic incident (%s)"%L("XTraffic","https://github.com/XAITraffic/XTraffic"))],
 "hass":[I("hass.png",1466,526,"Hierarchical adaptive sampling: framework overview","Flat and hierarchical system structures"),
         I("hass_iot.png",826,201,"IoT testbed: Raspberry Pi edge devices, testbed structure, and in-control versus out-of-control data","IoT testbed case")],
 "kappa":[I("kappa_model.png",1737,569,"SetPLM: keyword extraction in the encoder and keyword-based keyphrase generation in the decoder","Encoder-decoder model"),
          I("kappa.png",835,335,"KAPPA: portrait generation and portrait-based analytics","Framework overview"),
          I("kappa_result.svg",464,138,"Hyperparameter sensitivity on the expert-verified Patent-2k test set","Hyperparameter sensitivity")],
 "bsac":[I("bsac_bdrl.png",800,674,"Bilevel deep reinforcement learning: upper-level and lower-level agents in the BIMDP environment","Bilevel learning framework"),
         I("bsac_result.png",2400,2374,"Learning curves of the upper-level and lower-level agents on the laptop and electric-vehicle cases","Learning curves"),
         I("bsac_sensitivity.svg",1800,648,"Sensitivity of the product-design and remanufacturing objectives (laptop and electric-vehicle cases)","Sensitivity analysis")],
 "ijpe":[I("ijpe_policy.svg",330,132,"Policy network of the adapted SAC: reparameterization, action bounding and action discretization","Policy network"),
         I("ijpe_value.svg",302,183,"Value network with element-wise value estimation","Value network"),
         I("ijpe_problem.png",1224,741,"Hierarchical joint optimization of product design changes and the resilient supply chain","Joint design-change and supply-chain decisions"),
         I("ijpe_structure.png",831,426,"Design change propagation in the product structure","Design change propagation"),
         I("ijpe_result.png",1187,1084,"Objective values during training on the large-scale problem","Training curves")],
 "msom":[I("msom.png",296,158,"A bilevel supply chain system: platform as leader, supply chain members as followers","Bilevel supply chain system"),
         I("msom_result.svg",468,138,"Gap of objective values between training and testing for each supply chain member","Robustness comparison")],
 "causal":[I("causal_model.svg",440,146,"MAC framework: Meta-Debate Module and Debate-Coding Module","MAC framework"),
           I("causal_result.svg",456,166,"Average rank across five datasets and three LLMs","Average rank across datasets")],
}
# A main-page demo may combine two figures of a work into one wider panel.
MAIN={"bsac":dict(combo=[[DEMOS["bsac"][0],DEMOS["bsac"][1]]],fig="Bilevel learning framework and learning curves"),
      "ijpe":dict(cols=[[DEMOS["ijpe"][0],DEMOS["ijpe"][1]],[DEMOS["ijpe"][4]]],fig="Policy and value networks, and training curves")}
SHORT={"dispatchppo":"Collision-free dispatch for route-wise anomaly detection","scan":"SCAN: networked multi-agent anomaly detection","hass":"Hierarchical adaptive sampling (PAD)",
       "kappa":"KAPPA: patent analysis with keyphrase portraits","bsac":"Bilevel SAC for product design and remanufacturing","ijpe":"Design changes with a resilient supply chain",
       "msom":"Multi-level decision-making for supply chain resilience","causal":"Multi-agent causal discovery with LLMs"}

THEMES=[
 dict(slug="language-models",q="How to represent and predict",title="Multimodal data fusion and prediction",short="Multimodal data fusion",tech="Foundation models (LLMs, VLMs)",
      desc="Pretrained language models for keyphrase generation and patent analysis, and LLM agents that debate to discover causal structure.",
      cover="images/covers/language-models.png",fit="contain",keys=["kappa","causal"]),
 dict(slug="multi-agent",q="What to observe",title="Real-time anomaly detection",short="Real-time anomaly detection",tech="Deep reinforcement learning (RL)",
      desc="Hierarchical and cooperative agents that allocate limited resources and coordinate decisions in large systems.",
      cover="images/covers/multi-agent.png",fit="contain",keys=["hass","iise"]),
 dict(slug="supply-chain",q="How to act",title="Resilience of networked systems",short="Resilience of networked systems",tech="Stackelberg game, bilevel optimization",
      desc="Deep reinforcement learning for bilevel problems in product design, remanufacturing and resilient supply chains.",
      cover="images/covers/supply-chain.png",fit="contain",keys=["bsac","ijpe","msom"]),
 dict(slug="fleets",q="How to coordinate",title="Coordinated control of robot and drone fleets",short="Robot and drone fleet control",tech="Multi-agent RL, multi-robot path planning",
      desc="Dispatch and sampling policies that let fleets of mobile sensors detect anomalies quickly while keeping false alarms under control.",
      cover="images/covers/fleets.png",fit="contain",keys=["dispatchppo","scan"]),
]
PAGE_OF={k:"project-%s.html"%t["slug"] for t in THEMES for k in t["keys"]}

def media(m):
    if "cols" in m:   # columns of stacked figures, widths chosen so every column has the same height
        cols="".join('<div class="ccol" data-s="%.5f" data-n="%d" style="flex:%.4f 1 0">%s</div>'%(sum(x["h"]/x["w"] for x in col),len(col),1/sum(x["h"]/x["w"] for x in col),
              "".join('<a href="%s" data-lb="%s"><img src="%s" alt="" loading="lazy" style="aspect-ratio:%d/%d"></a>'%(x["image"],x["cap"],x["image"],x["w"],x["h"]) for x in col)) for col in m["cols"])
        return '<figure class="fig"><div class="media combo h">%s</div><figcaption>%s</figcaption></figure>'%(cols,m["fig"])
    if "combo" in m:
        parts="".join('<div class="crow">%s</div>'%"".join('<a href="%s" data-lb="%s" style="flex:%.4f 1 0"><img src="%s" alt="" loading="lazy" style="aspect-ratio:%d/%d"></a>'%(x["image"],x["cap"],x["w"]/x["h"],x["image"],x["w"],x["h"]) for x in row) for row in m["combo"])
        return '<figure class="fig"><div class="media combo">%s</div><figcaption>%s</figcaption></figure>'%(parts,m["fig"])
    w,h=_size(m); ar=' style="aspect-ratio:%d/%d"'%(w,h)
    fig='<figcaption>%s</figcaption>'%m["fig"] if m.get("fig") else ""
    if "video" in m:
        a='<a class="media" href="%s" data-lb="%s" data-video="%s"><video src="%s" poster="%s" muted loop playsinline autoplay preload="auto"%s></video></a>'%(m["full"],m["cap"],_hd(m["video"]),m["video"],m["poster"],ar)
    else:
        a='<a class="media" href="%s" data-lb="%s"><img src="%s" alt="" loading="lazy"%s></a>'%(m["image"],m["cap"],m["image"],ar)
    return '<figure class="fig" style="--ar:%.4f">%s%s</figure>'%(w/h,a,fig)

def award_html(p):
    if not p["award"]: return ""
    tag=('a','href="%s" target="_blank" rel="noopener" '%p["award_url"]) if p.get("award_url") else ('div','')
    return ('<%s %sclass="aw"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M7 6H4v2a3 3 0 0 0 3 3M17 6h3v2a3 3 0 0 1-3 3"/></svg>%s</%s>'%(tag[0],tag[1],p["award"].replace('<b class="win">Winner</b>',"Winner, "),tag[0]))
def std_links(p):
    """Paper, Code, Poster - in that order, only those that exist."""
    name={"DOI":"Paper","arXiv":"Paper","Paper":"Paper","Code":"Code","Poster":"Poster"}
    got={}
    for l,u in p["links"]:
        if not u.startswith("images/") and l in name: got.setdefault(name[l],u)
    return [(l,got[l]) for l in ("Paper","Code","Poster") if l in got]
def buttons(p,project=True):
    out="".join('<a href="%s" target="_blank" rel="noopener">%s</a>'%(u,l) for l,u in std_links(p))
    return out
def cite(p,link=True):
    ti=p["title"]
    if link and p["k"] in PAGE_OF: ti='<a href="%s#proj-%s">%s</a>'%(PAGE_OF[p["k"]],p["k"],ti)
    status=' <span class="st">(%s)</span>'%p["status"] if p["status"] else ""
    return '<h3 class="t">%s</h3><div class="au">%s</div><div class="ve">%s%s</div>%s'%(ti,p["au"],p["venue"],status,award_html(p))

def pub_html(p):
    k=p["k"]
    left=media(MAIN.get(k,DEMOS[k][0])) if k in DEMOS else '<figure class="fig"><span class="media"><img src="images/fulls/%s.jpg" alt="" loading="lazy"></span></figure>'%k
    return '<article class="pub" id="pub-%s"><div class="left">%s</div><div class="right">%s<div class="btns">%s</div></div></article>'%(k,left,cite(p),buttons(p))

def gallery(ms):
    """rows of one or two demos: two share a row only if the pair stays reasonably tall"""
    rows=[]; i=0
    while i<len(ms):
        a=ms[i]; wa,ha=_size(a)
        if i+1<len(ms):
            b=ms[i+1]; wb,hb=_size(b)
            if wa/ha+wb/hb<=4.7: rows.append('<div class="pairrow">%s%s</div>'%(media(a),media(b))); i+=2; continue
        rows.append('<div class="single">%s</div>'%media(a)); i+=1
    return '<div class="gallery">%s</div>'%"".join(rows)
def proj_html(p):
    return ('<article class="proj" id="proj-%s">%s<p class="abs">%s</p><div class="btns">%s</div>%s</article>'
            %(p["k"],cite(p,link=False),p["abs"]+' <a class="more" href="paper-%s.html">Paper page &rarr;</a>'%p["k"],buttons(p,project=False),'<div class="gallery"><div class="single">%s</div></div>'%media(MAIN.get(p["k"],DEMOS[p["k"]][0])) if p["k"] in DEMOS else ""))

# ---------------------------------------------------------------- page shell
DESC="Xin Xia - Ph.D. candidate in Industrial Engineering at the University of Wisconsin-Madison. Reliable decisions in budgeted systems: multimodal foundation models, statistical process control, bilevel optimization, and multi-agent reinforcement learning."
import hashlib
CSSV=hashlib.md5(open(os.path.join(ROOT,"assets","site.css"),"rb").read()).hexdigest()[:8]
_SIZE={}
def _opt(html):
    """Use the .webp copy of an image when one exists, and give every <img> its size and loading hints."""
    def webp(m):
        p=m.group(2); w=p+".webp"
        return m.group(1)+(w if os.path.exists(os.path.join(ROOT,w)) else p)+'"'
    html=re.sub(r'((?:src|href|poster)=")(images/[^"]+\.(?:png|jpe?g))"',webp,html)
    def img(m):
        tag=m.group(0); src=re.search(r'src="(images/[^"]+)"',tag)
        if not src: return tag
        p=src.group(1); add=""
        if "width=" not in tag and not p.endswith(".svg"):
            if p not in _SIZE:
                from PIL import Image
                _SIZE[p]=Image.open(os.path.join(ROOT,p)).size
            add+=' width="%d" height="%d"'%_SIZE[p]
        if "avatar" in p: add+=' fetchpriority="high"'
        else:
            add+=' decoding="async"'
        return tag[:-1].replace(' loading="lazy"','')+add+">"
    return re.sub(r'<img [^>]*>',img,html)
def shell(title,body,page):
    return _opt(_shell(title,body,page))
LAND='''<header class="land" id="top"><div class="land-bg" aria-hidden="true"></div><div class="land-in">
<div class="land-tx"><h1 class="land-h"><b>Xin</b> Xia</h1>
<p class="land-p">Reliable AI for decision-making in budgeted systems</p>
<ul class="land-ri" aria-label="Research interests"><li><a href="project-multi-agent.html">Multi-agent reinforcement learning</a></li><li><a href="project-fleets.html">Embodied AI and autonomous systems</a></li><li><a href="project-language-models.html">Foundation models (LLMs, VLMs)</a></li><li><a href="project-supply-chain.html">Data-driven optimization</a></li></ul>
<p class="land-cta"><a class="pri" href="#about">About me</a><a class="m" href="publications.html">Publications</a><a class="m" href="talks.html">Talks</a><a class="m" href="projects.html">Projects</a><a href="data/XinXia-CV.pdf" target="_blank" rel="noopener">CV</a></p></div>
<div class="land-ph"><img src="images/hero.webp" alt="Xin Xia" width="900" height="900" fetchpriority="high"><p class="land-cap"><span>Ph.D. candidate, UW-Madison</span><span>Industrial and Systems Engineering</span><a href="mailto:xxia65@wisc.edu">xxia65@wisc.edu</a></p></div></div>
<a class="land-cue" href="#about" aria-label="Scroll to the introduction"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></a></header>'''
def _shell(title,body,page):
    land=LAND if page=="index" else ""
    pre="" if page=="index" else "index.html"
    items=[("index.html","about"),("publications.html","publications"),("talks.html","talks"),("projects.html","projects"),("data/XinXia-CV.pdf","cv")]
    nav="".join('<li><a href="%s"%s>%s</a></li>'%(h+('" target="_blank" rel="noopener' if h.endswith(".pdf") else ""),' class="on"' if (page==n or (page=="index" and n=="about")) else "","CV" if n=="cv" else n.capitalize()) for h,n in items)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="shortcut icon" href="/favicon.ico?v=5">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png?v=5">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png?v=5">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png?v=5">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png?v=5">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png?v=5">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=5">
<link rel="manifest" href="/site.webmanifest?v=5">
<meta name="theme-color" content="#2F3A4A">
<script>(function(){{var t=null;try{{t=localStorage.getItem('theme');}}catch(e){{}}if(t!=='light'&&t!=='dark')t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';document.documentElement.setAttribute('data-theme',t);}})();</script>
<meta name="author" content="Xin Xia">
<meta name="description" content="{DESC}">
<meta property="og:title" content="{title}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://xxia99.com/images/avatar.jpg">
<link rel="preload" href="assets/fonts/roboto-normal-2.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css?v={CSSV}">
</head>
<body class="pg-{page}">
<nav class="nav"><div class="in"><a class="brand" href="index.html"><b>Xin</b> Xia</a><ul>{nav}</ul><button class="tgl" id="tgl" type="button" aria-label="Switch between light and dark mode" title="Light or dark mode"><svg class="i-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="i-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button></div></nav>
{land}
<main class="page">
{body}
</main>
<footer class="foot">&copy; 2026 Xin Xia</footer>
<div class="lb" id="lb"><img src="" alt=""><video controls loop playsinline></video><div class="cap"></div></div>
<script>
(function(){{var lb=document.getElementById('lb'),im=lb.querySelector('img'),vd=lb.querySelector('video'),cp=lb.querySelector('.cap');
var src=null,rm=matchMedia('(prefers-reduced-motion: reduce)').matches,EZ='cubic-bezier(.23,1,.32,1)';
function fromSrc(el){{var s=src.getBoundingClientRect(),t=el.getBoundingClientRect();if(!t.width||!s.width)return null;return 'translate('+(s.left-t.left)+'px,'+(s.top-t.top)+'px) scale('+(s.width/t.width)+','+(s.height/t.height)+')';}}
function zoomIn(el){{if(!src||rm)return;el.style.transition='none';el.style.transform='none';var f=fromSrc(el);if(!f)return;el.style.transformOrigin='top left';el.style.transform=f;el.getBoundingClientRect();el.style.transition='transform .36s '+EZ;el.style.transform='none';}}
function finish(){{lb.classList.remove('open','closing');im.src='';vd.pause();vd.removeAttribute('src');vd.load();lb.classList.remove('isvideo');[im,vd].forEach(function(el){{el.style.transition='';el.style.transform='';}});src=null;}}
function close(){{if(!lb.classList.contains('open')||lb.classList.contains('closing'))return;var el=lb.classList.contains('isvideo')?vd:im;if(src&&!rm&&document.body.contains(src)){{el.style.transition='none';el.style.transform='none';var f=fromSrc(el);if(f){{el.style.transformOrigin='top left';el.getBoundingClientRect();el.style.transition='transform .26s '+EZ;el.style.transform=f;lb.classList.add('closing');setTimeout(finish,250);return;}}}}finish();}}
document.querySelectorAll('a[data-lb]').forEach(function(a){{a.addEventListener('click',function(e){{e.preventDefault();var v=a.getAttribute('data-video');src=a.querySelector('img,video')||a;
if(v){{lb.classList.add('isvideo');vd.onloadedmetadata=function(){{zoomIn(vd);}};vd.src=v;vd.currentTime=0;vd.play().catch(function(){{}});}}else{{lb.classList.remove('isvideo');var h=a.getAttribute('href');im.style.width='';im.style.background='';im.onload=function(){{if(/\\.svg$/.test(h)&&im.naturalHeight){{var ar=im.naturalWidth/im.naturalHeight;im.style.width=Math.min(window.innerWidth*0.92,window.innerHeight*0.86*ar)+'px';im.style.background='#fff';}}zoomIn(im);}};im.src=h;}}
cp.textContent=a.getAttribute('data-lb')||'';lb.classList.add('open');}});}});
lb.addEventListener('click',function(e){{if(e.target!==vd)close();}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
var links=[].filter.call(document.querySelectorAll('.nav li a'),function(a){{return a.getAttribute('href').charAt(0)==='#';}}),secs=links.map(function(a){{return document.querySelector(a.getAttribute('href'));}});
function spy(){{if(!links.length)return;var y=window.scrollY+120,i=0;secs.forEach(function(s,j){{if(s&&s.offsetTop<=y)i=j;}});links.forEach(function(a,j){{a.classList.toggle('on',j===i);}});}}
window.addEventListener('scroll',spy,{{passive:true}});spy();
function fit(){{document.querySelectorAll('.media.combo.h').forEach(function(C){{var cols=[].slice.call(C.querySelectorAll('.ccol'));if(cols.length!==2)return;var g=14,r=10,W=C.clientWidth-16-g,s1=+cols[0].dataset.s,s2=+cols[1].dataset.s,e1=r*(cols[0].dataset.n-1),e2=r*(cols[1].dataset.n-1),w1=(W*s2+e2-e1)/(s1+s2);cols[0].style.flex='0 0 '+w1+'px';cols[1].style.flex='0 0 '+(W-w1)+'px';}});
document.querySelectorAll('.pairrow').forEach(function(L){{var figs=[].slice.call(L.querySelectorAll('.fig')),ars=figs.map(function(f){{return parseFloat(f.style.getPropertyValue('--ar'))||1.6;}}),sum=ars.reduce(function(a,b){{return a+b;}},0);
figs.forEach(function(f){{f.style.flex='';}});
if(window.innerWidth<=700){{L.classList.add('col');return;}}
L.classList.remove('col');var inner=L.clientWidth-14*(figs.length-1);figs.forEach(function(f,i){{f.style.flex='0 0 '+(inner*ars[i]/sum)+'px';}});}});}}
fit();window.addEventListener('resize',fit);window.addEventListener('load',fit);
function vload(v){{if(!v.getAttribute('src')&&v.getAttribute('data-src'))v.src=v.getAttribute('data-src');}}
if('IntersectionObserver' in window){{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{var v=e.target;if(e.isIntersecting){{vload(v);v.play().catch(function(){{}});}}else if(v.getAttribute('src')){{v.pause();}}}});}},{{threshold:.15}});document.querySelectorAll('main video').forEach(function(v){{io.observe(v);}});}}else{{document.querySelectorAll('main video').forEach(function(v){{vload(v);v.play().catch(function(){{}});}});}}
if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches){{document.documentElement.classList.add('js');
var rv=[].slice.call(document.querySelectorAll('main section,.bcard,.pcard.mini,.bbar,.pub,.proj'));rv.forEach(function(e){{e.classList.add('rv');}});
var ro=new IntersectionObserver(function(es){{var n=0;es.forEach(function(en){{if(!en.isIntersecting)return;var e=en.target;ro.unobserve(e);e.style.transitionDelay=(n++*80)+'ms';e.classList.add('in');
setTimeout(function(){{e.classList.remove('rv','in');e.style.transitionDelay='';}},800+n*80);}});}},{{threshold:.06,rootMargin:'0px 0px -6% 0px'}});
rv.forEach(function(e){{ro.observe(e);}});}}
var nl=document.getElementById('newslist'),nb=document.getElementById('nmore');if(nl&&nb){{nl.classList.add('nc');nb.hidden=false;nb.addEventListener('click',function(){{var o=nl.classList.toggle('open');nb.setAttribute('aria-expanded',o?'true':'false');nb.textContent=o?'Show fewer':'Show '+nb.getAttribute('data-n')+' earlier';if(!o){{var r=document.getElementById('news').getBoundingClientRect();if(r.top<0)window.scrollTo(0,window.scrollY+r.top-90);}}}});}}
var ld=document.getElementById('top');if(ld){{var lf=function(){{document.documentElement.classList.toggle('past',window.scrollY>(ld.offsetHeight-120));}};lf();window.addEventListener('scroll',lf,{{passive:true}});}}
var fl=document.getElementById('flt');if(fl){{fl.addEventListener('click',function(e){{var b=e.target.closest('button');if(!b)return;var f=b.getAttribute('data-f');
[].forEach.call(fl.children,function(x){{x.setAttribute('aria-pressed',x===b?'true':'false');}});
[].forEach.call(document.querySelectorAll('#research .yg'),function(g){{var n=0;[].forEach.call(g.querySelectorAll('.pub'),function(p){{var on=!f||(' '+p.getAttribute('data-t')+' ').indexOf(' '+f+' ')>-1;p.hidden=!on;if(on){{n++;p.classList.remove('fin');void p.offsetWidth;p.classList.add('fin');}}}});g.hidden=!n;}});}});}}
var tg=document.getElementById('tgl'),mt=document.querySelector('meta[name="theme-color"]');
function paint(){{var d=document.documentElement.getAttribute('data-theme')==='dark';if(mt)mt.setAttribute('content',d?'#12161c':'#2F3A4A');if(tg)tg.setAttribute('aria-pressed',d?'true':'false');}}
paint();if(tg)tg.addEventListener('click',function(){{var n=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';document.documentElement.classList.add('th');document.documentElement.setAttribute('data-theme',n);try{{localStorage.setItem('theme',n);}}catch(e){{}}paint();setTimeout(function(){{document.documentElement.classList.remove('th');}},350);}});
}})();
</script>
{CFWA}</body>
</html>
"""

# ---------------------------------------------------------------- main page
FOCUS=[("What to sense","Resource-limited anomaly detection: a small monitoring budget is allocated across many data streams so that changes are found quickly.","project-multi-agent.html"),
       ("How to coordinate","Coordinated fleet control: robots and drones decide where to go next, without collisions and with false alarms under control.","project-fleets.html"),
       ("How to represent","Document representation and analytics: foundation models turn long, multi-level documents into compact portraits.","project-language-models.html")]
AW1='https://www.linkedin.com/posts/informs-quality-statistics-and-reliability-qsr_informs-quality-statistics-and-reliability-activity-7524611375281881088-RDX0'
AW2='https://myemail.constantcontact.com/QCRE-News---May-2025.html?aid=vKcqr1w06AU&amp;soid=1101700049774#:~:text=Interactive%20Resource%20Planning%20and%20Change%20Detection'
FOUR=(' My work covers four directions: <a href="project-fleets.html">robot and drone fleets for anomaly detection</a>, <a href="project-multi-agent.html">multi-agent systems for decision making</a>, <a href="project-language-models.html">foundation models and large language models</a>, and <a href="project-supply-chain.html">AI-driven supply chain management</a>.') if os.environ.get("PLAN","c")=="c" else ""
hero=f"""<section id="about"><header class="hero solo"><div><h2>About me</h2>
<p>I am a Ph.D. candidate in <a href="https://engineering.wisc.edu/departments/industrial-systems-engineering/">Industrial and Systems Engineering</a> at the University of Wisconsin-Madison, advised by <a href="https://kaibo.ie.wisc.edu/index.html">Prof. Kaibo Liu</a>. I received my M.Sc. in Electrical and Computer Engineering from Georgia Tech and my B.Eng. in Electrical Engineering and Automation from Tianjin University.</p>
<p class="thesis">My research develops <b>reliable AI for decision-making in budgeted systems</b>, where information acquisition is constrained and decisions incur costs.</p>
<p>This raises four questions: how to represent heterogeneous data, what to observe, how to act, and how to coordinate.</p>
<p>I pursue two connected lines of work.</p>
<div class="lines"><div class="lw"><b>Representation and prediction</b><p>Multimodal data fusion built on foundation models (LLMs, VLMs), with applications in <a href="project-language-models.html">interpretable knowledge discovery from unstructured data</a> and clinical decision support.</p></div><div class="lw"><b>AI-driven decision-making</b><p>Multi-agent reinforcement learning and data-driven optimization with statistical guarantees for sensing, acting, and coordination, with applications in <a href="project-fleets.html">embodied AI for autonomous fleets of robots and drones</a> and resilient networked systems in <a href="project-multi-agent.html">manufacturing</a> and <a href="project-supply-chain.html">supply chains</a>.</p></div></div>
<p>My work has appeared in NeurIPS, <em>Technometrics</em>, <em>IEEE Transactions on Engineering Management</em>, and the <em>International Journal of Production Economics</em>. It received the <a class="hot" href="{AW1}" target="_blank" rel="noopener">INFORMS QSR Best Refereed Paper Award</a> (2026) and was a finalist in the <a class="hot" href="{AW2}" target="_blank" rel="noopener">IISE QCRE Best Track Paper Competition</a> (2025). I serve as a reviewer for NeurIPS, <em>IEEE Transactions on Automation Science and Engineering</em>, <em>PNAS</em>, and <em>PNAS Nexus</em>.</p>
<p class="links"><a href="mailto:xxia65@wisc.edu">Email</a><a href="data/XinXia-CV.pdf">CV</a><a href="https://scholar.google.com/citations?user=baRH_vIAAAAJ&amp;hl=en">Google Scholar</a><a href="https://github.com/xxia99">GitHub</a><a href="https://www.linkedin.com/in/xin-xia-678546204/" target="_blank" rel="noopener">LinkedIn</a><a href="https://orcid.org/0009-0006-2910-7778" target="_blank" rel="noopener">ORCID</a></p>
</div></header></section>"""
VEN={"fleets":"NeurIPS &middot; INFORMS","multi-agent":"Technometrics &middot; IISE Trans.","language-models":"IJDS &middot; arXiv","supply-chain":"IEEE TEM &middot; IJPE &middot; M&amp;SOM"}
PLAN=os.environ.get("PLAN","c")   # a: directions with papers (text)   b: bar and four boxes   c: nothing
NICK={"dispatchppo":"DispatchPPO (NeurIPS 2026)","scan":"SCAN (INFORMS 2026)","hass":"Hierarchical adaptive sampling (Technometrics)","iise":"Multi-stage manufacturing coordination (IISE Trans., under review)",
      "kappa":"KAPPA (IJDS, major revision)","causal":"Multi-agent causal discovery (arXiv 2024)","bsac":"BSAC (IEEE TEM 2025)","ijpe":"Design changes with resilient supply chains (IJPE 2025)","msom":"Multi-level supply chain decisions (M&amp;SOM, submitted)"}
if PLAN=="a":
    roadmap='<section id="directions"><ul class="dirs">'+"".join('<li><a class="dn" href="project-%s.html">%s</a><span>%s</span></li>'%(t["slug"],t["title"],", ".join('<a href="project-%s.html#proj-%s">%s</a>'%(t["slug"],k,NICK[k]) for k in t["keys"])) for t in THEMES)+'</ul></section>'
elif PLAN=="b":
    roadmap=('<section id="directions" class="dia"><div class="dtop"><b>Reliable decisions in budgeted systems</b><span>where sensing and action resources are limited</span></div><div class="dcols">'
      +"".join('<a class="dcol" href="project-%s.html"><div class="dbox">%s</div></a>'%(t["slug"],t["title"]) for t in THEMES)+'</div></section>')
else:
    roadmap=""
NEWS_SHOWN=4
news=('<section id="news"><h2>News</h2><div class="news" id="newslist">'
      +"".join('<div class="d%s">%s</div><div%s>%s</div>'%(" more" if i>=NEWS_SHOWN else "",d,' class="more"' if i>=NEWS_SHOWN else "",t) for i,(d,t) in enumerate(NEWS))
      +'</div>'+(f'<button class="nmore" id="nmore" type="button" hidden aria-expanded="false" aria-controls="newslist" data-n="{len(NEWS)-NEWS_SHOWN}">Show {len(NEWS)-NEWS_SHOWN} earlier</button>' if len(NEWS)>NEWS_SHOWN else '')+'</section>')
SELECTED=["dispatchppo","scan","hass","kappa","bsac","causal"]
TOPIC=[("marl","Multi-agent reinforcement learning"),("embodied","Embodied AI and autonomous systems"),("fm","Foundation models (LLMs, VLMs)"),("opt","Data-driven optimization")]
PTOPIC={"dispatchppo":"marl embodied","scan":"marl embodied","hass":"marl","kappa":"fm","bsac":"opt","causal":"fm"}
research='<section id="research"><h2>Selected research <a class="more" href="publications.html">All publications &rarr;</a></h2><div class="flt" id="flt" role="group" aria-label="Filter by research interest"><button type="button" data-f="" aria-pressed="true">All</button>'+"".join('<button type="button" data-f="%s" aria-pressed="false">%s</button>'%t for t in TOPIC)+'</div>'
for g in ["2026","2025","2024","Under review"]:
    items=[p for p in PUBS if p["year"]==g and p["k"] in SELECTED]
    if items: research+='<div class="yg"><div class="year">'+g+'</div><div class="pubs">'+"".join(pub_html(p).replace('<article class="pub"','<article class="pub" data-t="'+PTOPIC[p["k"]]+'"',1) for p in items)+'</div></div>'
research+='</section>'
TIMELINE=[("2025 - present","Ph.D. candidate, University of Wisconsin-Madison","Industrial and Systems Engineering. Advisor: Prof. Kaibo Liu.","uw.svg","University of Wisconsin-Madison",""),
          ("2022 - 2025","Research assistant, Tsinghua University",'<a href="https://thu-sail-lab.github.io/home/" target="_blank" rel="noopener">SAIL Lab</a>. Advisor: <a href="https://www.ie.tsinghua.edu.cn/eng/info/1051/1031.htm" target="_blank" rel="noopener">Prof. Chen Zhang</a>.',"tsinghua.png","Tsinghua University",""),
          ("2021 - 2022","AI researcher intern, Ping An Technology","Computer vision and multimodal models.","pingan-tech.png","Ping An Technology"," wide pa"),
          ("2020 - 2022","M.Sc., Georgia Institute of Technology","Electrical and Computer Engineering.","gatech.svg","Georgia Institute of Technology",""),
          ("2016 - 2020","B.Eng., Tianjin University","Electrical Engineering and Automation.","tju.png","Tianjin University","")]
cv='<section id="experience"><h2>Experience</h2><div class="vt">'+"".join(
   '<div class="vi"><img class="vl%s" src="images/logos/%s" alt="%s" loading="lazy"><div class="vd">%s</div><div class="vh">%s</div><div class="vs">%s</div></div>'%(w,lg,alt,d,h,sub) for d,h,sub,lg,alt,w in TIMELINE)+'</div></section>'
open(os.path.join(ROOT,os.environ.get("OUT","index.html")),"w").write(shell("Xin Xia","\n".join([hero,roadmap,news,research,cv]),"index"))

# ---------------------------------------------------------------- projects: gallery + one page per theme
BYK0={p["k"]:p for p in PUBS}
MINI={"setplm":"Keyphrase generation with a pretrained language model.","berthrl":"Berth and quay-crane scheduling with reinforcement learning.","dcgan":"Scenario generation with a Wasserstein DCGAN."}
def card(t):
    venues=" &middot; ".join(dict.fromkeys(BYK0[k]["badge"] for k in t["keys"]))
    return ('<a class="pcard" href="project-%s.html"><div class="cover %s"><img src="%s" alt="" loading="lazy"></div><div class="b"><h3>%s</h3></div></a>'
            %(t["slug"],t["fit"],t["cover"],t["title"]))
proj='<section id="projects"><h1>Projects</h1>'
def _chips(txt):
    parts=re.split(r',\s*(?![^()]*\))',txt)
    return '<div class="bchips">'+"".join('<span>%s</span>'%(p[0].upper()+p[1:]) for p in parts if p)+'</div>'
def _bcard(i,t):
    return ('<a class="bcard" href="project-%s.html"><div class="bhead"><span class="bnum">%d</span><span class="bq">%s</span></div><div class="bimg"><img src="%s" alt="" loading="lazy"></div><div class="bt">%s</div>%s</a>'
            %(t["slug"],i,t["q"],t["cover"],t["short"],_chips(t["tech"])))
proj+=('<h2><span><b>Research projects:</b> reliable AI for decision-making in budgeted systems</span></h2><div class="bento">'
  '<div class="bcol"><div class="bbar">Representation and prediction</div><div class="brow" style="--n:1">'+_bcard(1,THEMES[0])+'</div></div>'
  '<div class="bcol"><div class="bbar">AI-driven decision-making</div><div class="brow" style="--n:3">'+"".join(_bcard(i+2,t) for i,t in enumerate(THEMES[1:]))+'</div></div></div>')
MINIS=[("Energy system scenario generation","DCGAN, Wasserstein GAN","https://github.com/xxia99/DCGAN-for-Scenario-Generation",
        dict(video="images/mini/gan_training.mp4",poster="images/mini/gan_training.jpg",cap="Generated daily scenarios during training")),
       ("Patient outcome prediction from text","Tabular-to-text conversion, BERT embeddings, MLP classifier","https://github.com/xxia99/Text-Classification",
        dict(image="images/mini/text_curves.png",cap="Training loss with and without a pretrained embedding layer")),
       ("Power outage forecasting","Time-series foundation models, LoRA, TCN","https://github.com/xxia99/weather_prediction",
        dict(image="images/mini/outage_forecast.svg",cap="Observed and forecast outages over ten validation days"))]
def _mini(n,d,u,m):
    cov=""
    if m and "video" in m:
        cov='<a class="cover contain" href="%s" data-lb="%s" data-video="%s"><video src="%s" poster="%s" muted loop playsinline autoplay preload="auto"></video></a>'%(m["poster"],m["cap"],_hd(m["video"]),m["video"],m["poster"])
    elif m:
        cov='<a class="cover contain" href="%s" data-lb="%s"><img src="%s" alt="%s" loading="lazy"></a>'%(m["image"],m["cap"],m["image"],m["cap"])
    t='<a href="%s" target="_blank" rel="noopener">%s</a>'%(u,n) if u else n
    return '<div class="pcard mini">%s<div class="b"><h3>%s</h3>%s</div></div>'%(cov,t,_chips(d))
proj+='<h2><b>Mini projects</b></h2><div class="pgrid three">'+"".join(_mini(*x) for x in MINIS)+'</div></section>'
open(os.path.join(ROOT,"projects.html"),"w").write(shell("Projects - Xin Xia",proj,"projects"))
for ti,t in enumerate(THEMES):
    body='<section><p class="back"><a href="projects.html">&larr; All projects</a></p><h1 class="ph">%s</h1>'%t["title"]
    pv=THEMES[ti-1] if ti>0 else None; nx=THEMES[ti+1] if ti<len(THEMES)-1 else None
    pn='<nav class="pn">%s%s</nav>'%(('<a class="pv" href="project-%s.html"><span>Previous project</span>&larr; %s</a>'%(pv["slug"],pv["title"])) if pv else '<span></span>',
                                     ('<a class="nx" href="project-%s.html"><span>Next project</span>%s &rarr;</a>'%(nx["slug"],nx["title"])) if nx else '<span></span>')
    body+="".join(proj_html(BYK0[k]) for k in t["keys"])+pn+'</section>'
    open(os.path.join(ROOT,"project-%s.html"%t["slug"]),"w").write(shell("%s - Xin Xia"%t["title"],body,"projects"))


# ---------------------------------------------------------------- paper pages (one page per paper, grouped under its project)
def _pfig(img,cap,w,h,cls=""):
    return '<figure class="pp-fig%s"><a href="%s" data-lb="%s"><img src="%s" alt="%s" loading="lazy" style="aspect-ratio:%d/%d"></a><figcaption>%s</figcaption></figure>'%(cls,img,cap,img,cap,w,h,cap)
def _pvid(v,poster,full,cap,w,h,link=""):
    return '<figure class="pp-fig"><a class="media" href="%s" data-lb="%s" data-video="%s"><video src="%s" poster="%s" muted loop playsinline autoplay preload="auto" style="aspect-ratio:%d/%d"></video></a><figcaption>%s</figcaption></figure>'%(full,cap,_hd(v),v,poster,w,h,link or cap)
DEMO_DEFAULT=(5,3,30,5,'scatter1')
def _demo_idx():
    import json
    return json.load(open(os.path.join(ROOT,'data','demo','runs','index.json')))
def _demo_index():
    """Which recorded settings exist, as one 0/1 string per (UAVs, shift) file, ordered abnormal count x change point x layout."""
    import json
    ix=_demo_idx(); av={}
    for k,keys in ix['avail'].items():
        ks=set(keys); bits=''.join('1' if '%d_%d_%s'%(A,nu,l) in ks else '0' for A in ix['anoms'] for nu in ix['nus'] for l in ix['layouts'])
        if '1' in bits and k.split('_')[1]!='1': av[k]=bits
    Ns=sorted({int(k.split('_')[0]) for k in av}); sh=sorted({int(k.split('_')[1]) for k in av})
    return json.dumps({'Ns':Ns,'shifts':sh,'nus':ix['nus'],'anoms':ix['anoms'],'layouts':ix['layouts'],'avail':av},separators=(',',':'))
def _demo_default():
    """The run shown before any setting is chosen, embedded so the figure draws without a request."""
    import json
    N,sh,nu,A,lay=DEMO_DEFAULT; f=json.load(open(os.path.join(ROOT,'data','demo','runs','n%d_s%d.json'%(N,sh)))); key='%d_%d_%s'%(A,nu,lay)
    if key not in f['runs']: key=sorted(f['runs'])[0]; A,nu,lay=int(key.split('_')[0]),int(key.split('_')[1]),key.split('_')[2]
    r=f['runs'][key]; p=r['p']; T=len(p)//(2*N)-1
    pos=[[int(p[(t*N+n)*2:(t*N+n)*2+2]) for n in range(N)] for t in range(T+1)]
    return json.dumps({'N':N,'shift':sh,'nu':nu,'A':A,'lay':lay,'anom':r['anom'],'al':r['al'],'pos':pos,'stat':[v/10 for v in r['s']]},separators=(',',':'))
REPLAY_HTML="""<section class="pp-sec" id="replay"><h2>DispatchPPO detects anomalies quickly when they occur at unknown locations and times</h2><div class="pp-tx"><p>A fleet of UAVs monitors a 10&times;10 grid, and each UAV observes only the location it visits. At some time step, anomalies occur at a few locations. The time and the locations are unknown to the fleet, and an alarm is triggered once the detection statistic exceeds the threshold. Try it in three steps with the learned policy, which runs on a server.</p></div>
<div class="pf" id="rp">
<form class="pc" id="pc" onsubmit="return false">
<div class="pc-h"><i>1</i><span>Choose the fleet size and place the UAVs</span></div>
<div class="pc-r"><span class="pc-l">Number of UAVs</span><div class="pc-seg" data-k="N"><button type="button" data-v="2">2</button><button type="button" data-v="5">5</button><button type="button" data-v="10">10</button></div></div>
<div class="pc-r pc-lay"><span class="pc-l">Initial locations of UAVs</span><div class="pc-row"><div class="pc-x"><button type="button" id="pc-rand">Random</button></div><span class="pc-or">or drag a UAV on the grid</span></div></div>
<div class="pc-h"><i>2</i><span>Decide when and where the anomalies occur, and their magnitude <small>Unknown to the fleet.</small></span></div>
<div class="pc-r pc-two"><label class="pc-l" for="pc-nu">Anomalies occur at</label><div class="pc-pair"><div class="pc-sl"><input type="range" id="pc-nu" min="10" max="60" step="1" value="30"><output id="pc-nuv" for="pc-nu">time step 30</output></div><div class="pc-sl pc-mag"><label class="pc-l2" for="pc-sh">Magnitude</label><span>small</span><input type="range" id="pc-sh" min="2" max="4" step="0.05" value="3"><span>large</span></div></div></div>
<div class="pc-r pc-lay"><span class="pc-l">Locations of the anomalies</span><div class="pc-row"><div class="pc-x"><button type="button" id="pc-scat">Randomly scattered</button><button type="button" id="pc-clus">Randomly clustered</button></div><span class="pc-or">or click the grid to add or remove one</span><span class="pc-ct" id="pc-cc"></span></div></div>
<div class="pc-h"><i>3</i><span>Run the learned policy in your setting</span></div>
<div class="pc-r pc-go"><button type="button" class="rp-play" id="pc-run">Run</button><button type="button" class="pc-rs" id="pc-reset">Reset</button><span class="pc-msg" id="pc-msg" aria-live="polite"></span></div>
</form>
<div class="pf-panel"><ul class="pf-leg"><li><i class="l-n"></i>Normal Location</li><li><i class="l-a"></i>Anomaly</li><li><svg width="34" height="12" viewBox="0 0 34 12" aria-hidden="true"><path d="M1 6h27" stroke="#4d96da" stroke-width="2.2" fill="none"/><path d="M24 1.5l6 4.5-6 4.5" stroke="#4d96da" stroke-width="2.2" fill="none" stroke-linejoin="round" stroke-linecap="round"/></svg>Movement</li><li><i class="l-d"></i>Destination</li></ul>
<div class="pf-main"><div class="pf-g"><p class="pf-t">At time step <i>t</i> = <span id="rp-t">0</span></p><svg class="pf-grid" id="rp-grid" viewBox="-2 -2 504 504" role="img" aria-label="Positions of the UAVs on the grid at the current time step"></svg><p class="pf-m" id="rp-m"></p><p class="pf-rt" id="rp-rt"></p></div>
<div class="pf-c"><svg class="pf-chart" id="rp-chart" viewBox="0 0 560 410" role="img" aria-label="System-level detection statistic over the time steps of the episode"></svg></div></div></div>
<p class="rp-status" id="rp-status" aria-live="polite"></p>
<div class="rp-ctl"><button type="button" class="rp-play" id="rp-play">Play</button><input type="range" id="rp-range" min="0" max="1" value="0" step="1" aria-label="Time step of the episode"><span class="rp-step" id="rp-step"></span></div>
<p class="rp-note" id="rp-note"></p></div>
<script type="application/json" id="ep">@@EP@@</script><script type="application/json" id="pmeta">@@META@@</script><script type="application/json" id="pidx">@@IDX@@</script></section>"""
DECODE_HTML=_pfig("images/fulls/dp_dispatchnet.svg","DispatchNet architecture. The encoder extracts spatial features and inter-UAV interactions from the observation. An autoregressive decoder then samples per-UAV moves with a dynamic feasibility mask, producing a collision-free joint move without enumerating all joint moves.",2149,715)
DECIDE_HTML=('<div class="pp-tx"><p>Try the decoder in three steps.</p></div><div class="pf dm" id="dm"><form class="pc" onsubmit="return false">'
    +'<div class="pc-h"><i>1</i><span>Place the 3 UAVs by dragging them on the grid</span></div>'
    +'<div class="pc-h"><i>2</i><span>Turn DispatchNet on or off</span></div><div class="pc-r pc-r1"><div class="pc-seg" data-r="mask" role="group" aria-label="DispatchNet"><button type="button" data-v="1">On</button><button type="button" data-v="0">Off</button></div></div>'
    +'<div class="pc-h"><i>3</i><span>Play the joint moves</span></div><ul class="pc-ex"><li><b>Play</b> decodes one joint move: the decoder assigns a move to UAV 1, UAV 2 and UAV 3 sequentially, and then all three UAVs move together. During decoding, the button becomes <b>Next UAV</b>: click it to decode the next UAV at once.</li><li><b>Play 10 moves fast</b> decodes ten joint moves in a row without showing the decoding of each UAV, and stops at the first collision.</li><li><b>Reset</b> returns the UAVs to their initial locations and clears the count.</li></ul><div class="pc-r pc-go"><button type="button" class="rp-play" data-r="play">Play</button><button type="button" class="pc-rs" data-r="quick">Play 10 moves fast</button><button type="button" class="pc-rs" data-r="reset">Reset</button><span class="pc-msg" data-r="msg" aria-live="polite"></span></div></form>'
    +'<div class="pf-panel"><ul class="pf-leg"><li><i class="l-p"></i>Score</li><li><i class="l-k"></i>Reserved Location</li><li><i class="l-d"></i>Destination</li></ul>'
    +'<div class="pf-main"><div class="pf-g"><svg class="pf-grid" id="dm-grid" data-r="grid" role="img" aria-label="Three UAVs on a grid while their moves are decided one after another"></svg></div>'
    +'<div class="dm-side"><svg class="dm-strip" data-r="strip" role="img" aria-label="Decoder: for each UAV its scores over 9 local moves, the mask, the masked scores and the sampled move"></svg></div></div></div>'
    +'<p class="rp-status" data-r="status" aria-live="polite"></p><p class="rp-note">Illustration with an untrained DispatchNet on a 3&times;3 grid.</p></div>'
    +'<script type="application/json" id="dm-tab">'+open(os.path.join(ROOT,'data','demo','dispatchnet_untrained_g3n3.json')).read()+'</script>')
def _thm(i,title,text,leg,side,note,cls=''):
    return ('<h3>%s</h3><div class="pp-tx"><p>%s</p></div><div class="pf th%s" id="%s">'%(title,text,cls,i)
        +'<div class="pf-panel"><ul class="pf-leg">%s</ul><div class="pf-main"><div class="pf-g"><svg class="pf-grid" id="%s-grid" data-r="grid" role="img" aria-label="%s, illustrated on a small grid"></svg></div>%s</div></div>'%(leg,i,title,side)
        +'<p class="rp-status" data-r="status" aria-live="off"></p><p class="rp-note">%s</p></div>'%note)
_LEG='<li><i class="l-n"></i>Normal Location</li><li><i class="l-a"></i>Anomaly</li>'
_CH=lambda a:'<div class="th-side"><svg class="pf-chart" data-r="side" viewBox="0 0 560 300" role="img" aria-label="%s"></svg></div>'%a
THM_HTML=(_thm('ta','Persistent coverage','Every location is visited infinitely often, and no location is permanently ignored.','<li><i class="l-p"></i>Hit Rate</li>','','Illustration with 2 UAVs on a 4&times;4 grid. The number at each location is its hit rate, the fraction of time steps at which it is observed.',' solo')
    +_thm('tb','Evidence-based focusing','After the change, UAVs keep revisiting an isolated affected location whose evidence is locally dominant.',_LEG,_CH('Probability of the stay move at the affected location over the time steps, with the limit of the theorem'),'Illustration with 1 UAV on a 3&times;3 grid and exploration rate 0.1. The evidence increases by 2 at each observation of the affected location.')
    +_thm('td','Corollary: clustered anomalies','As a corollary of evidence-based focusing, clustered anomalies are still detected; UAVs may move within the cluster.',_LEG,_CH('Statistic over the time steps, with the detection threshold'),'Illustration with 1 UAV on a 4&times;4 grid and detection threshold 8. The evidence increases by 1 at each observation of an affected location.')
    +_thm('tc','Detection-delay bound','The mean detection delay is bounded, and a higher hit rate on the affected location gives a smaller bound.',_LEG,_CH('Statistic over the time steps for three hit rates, with the detection threshold'),'Illustration with detection threshold 8. The statistic increases by 1 at each observation of the affected location.',' wide'))
PAPER_JS="""<script>
(function(){var NS='http://www.w3.org/2000/svg',BLUE='#4d96da',GRID='#adb0b6',ABN='#e59490',LINE='#4b92c3',ICON='images/demo/drone.svg';
var RM=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function mk(t,a,p){var e=document.createElementNS(NS,t);for(var k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e;}
function gridSvg(svg,G,C){var W=G*C;mk('rect',{x:0,y:0,width:W,height:W,fill:'#fff'},svg);var cells=mk('g',{},svg),lines=mk('g',{stroke:GRID,'stroke-width':2},svg),i;
for(i=0;i<=G;i++){mk('line',{x1:0,y1:i*C,x2:W,y2:i*C},lines);mk('line',{x1:i*C,y1:0,x2:i*C,y2:W},lines);}
var defs=mk('defs',{},svg);[['b',BLUE],['g','#7d7d7d']].forEach(function(m){var mm=mk('marker',{id:svg.id+'-'+m[0],viewBox:'0 0 10 10',refX:8,refY:5,markerWidth:5.2,markerHeight:5.2,orient:'auto'},defs);mk('path',{d:'M1 1L9 5L1 9',fill:'none',stroke:m[1],'stroke-width':1.8,'stroke-linejoin':'round','stroke-linecap':'round'},mm);});
var cp=mk('clipPath',{id:svg.id+'-c'},defs);mk('circle',{cx:C/2,cy:C/2,r:C*0.42},cp);
return {cells:cells,tail:mk('g',{},svg),under:mk('g',{},svg),icons:mk('g',{},svg),over:mk('g',{},svg)};}
function icon(L,svg,C){var g=mk('g',{'class':'pf-u'},L.icons);mk('image',{href:ICON,x:C*0.08,y:C*0.08,width:C*0.84,height:C*0.84,'clip-path':'url(#'+svg.id+'-c)'},g);return g;}
function arrow(L,svg,C,a,b,col,dash,delay){var ax=a[1]*C+C/2,ay=a[0]*C+C/2,bx=b[1]*C+C/2,by=b[0]*C+C/2,dx=bx-ax,dy=by-ay,n=Math.sqrt(dx*dx+dy*dy);if(n<1)return;var s=C*0.44,e=dash?C*0.12:C*0.2;
var at={x1:ax+dx/n*s,y1:ay+dy/n*s,x2:bx-dx/n*e,y2:by-dy/n*e,stroke:dash?'#b9b9b9':(col=='b'?BLUE:'#7d7d7d'),'stroke-width':C*0.05,'stroke-linecap':'round','class':'pf-ar'};if(dash)at['stroke-dasharray']=(C*0.08)+' '+(C*0.08);else at['marker-end']='url(#'+svg.id+'-'+col+')';
var l=mk('line',at,L.under);l.style.transformOrigin=ax+'px '+ay+'px';if(delay)l.style.animationDelay=delay+'ms';return l;}
function dot(L,C,p,delay){var c=mk('circle',{cx:p[1]*C+C/2,cy:p[0]*C+C/2,r:C*0.15,fill:BLUE,'class':'pf-dot'},L.over);if(delay)c.style.animationDelay=delay+'ms';return c;}
function clear(g){while(g.firstChild)g.removeChild(g.firstChild);}
function place(g,p,C){g.style.transform='translate('+p[1]*C+'px,'+p[0]*C+'px)';}
/* ---- episode replay and live runs ---- */
(function(){var el=document.getElementById('rp');if(!el)return;var REC=JSON.parse(document.getElementById('ep').textContent),META=JSON.parse(document.getElementById('pmeta').textContent),G=10,C=50,K=G*G,TAIL=7,STEP=560,HOLD=150,MAXT=260;
var svg=document.getElementById('rp-grid'),ch=document.getElementById('rp-chart'),q=function(id){return document.getElementById(id);},range=q('rp-range'),play=q('rp-play'),msg=q('pc-msg');
var DEF={cells:REC.anom.slice()},st={N:REC.N,shift:REC.shift,nu:REC.nu,cells:REC.anom.slice(),start:REC.pos[0].slice(),arl0:'370'},IDX=JSON.parse(document.getElementById('pidx').textContent),files={},raw=null,D=null,V=null,timer=null,mv=null,now=0,editing=false,busy=false;
function rc(k){return [Math.floor(k/G),k%G];}
function thr(N,a){var m=META[N];return (m.thresholds&&m.thresholds[a])?m.thresholds[a].threshold:m.H370;}
/* build the figure for one episode D = {N, nu, threshold, alarm, T, anom[], pos[t][n]=cell, stat[t]} */
function build(){clear(svg);clear(ch);var L=gridSvg(svg,G,C),N=D.N,T=D.T,i,uavs=[];
var abn=D.anom.map(function(k){return mk('rect',{x:(k%G)*C,y:Math.floor(k/G)*C,width:C,height:C,fill:ABN,opacity:0,'class':'pf-ab'},L.cells);});
for(i=0;i<N;i++)uavs.push(icon(L,svg,C));
var x0=80,x1=540,y0=20,y1=344,top=Math.min(Math.max(D.threshold*1.15,Math.max.apply(null,D.stat.slice(0,T+1))),D.threshold*2.5),ys=top>42?10:5,ymax=Math.ceil(top/ys)*ys+ys*0.2,xs=T>240?50:(T>100?20:10),xm=Math.max(xs,Math.ceil(T/xs)*xs);
var X=function(t){return x0+t/xm*(x1-x0);},Y=function(v){return y1-Math.min(v,ymax)/ymax*(y1-y0);};
mk('rect',{x:0,y:0,width:560,height:410,fill:'#fff'},ch);
for(i=0;i<=xm;i+=xs){mk('line',{x1:X(i),y1:y0,x2:X(i),y2:y1,stroke:'#e6e6e6'},ch);mk('line',{x1:X(i),y1:y1,x2:X(i),y2:y1+6,stroke:'#000'},ch);mk('text',{x:X(i),y:y1+24,'text-anchor':'middle','class':'tk'},ch).textContent=i;}
for(i=0;i<ymax;i+=ys){mk('line',{x1:x0,y1:Y(i),x2:x1,y2:Y(i),stroke:'#e6e6e6'},ch);mk('line',{x1:x0-6,y1:Y(i),x2:x0,y2:Y(i),stroke:'#000'},ch);mk('text',{x:x0-11,y:Y(i)+5,'text-anchor':'end','class':'tk'},ch).textContent=i;}
if(D.nu<=xm)mk('line',{x1:X(D.nu),y1:y0,x2:X(D.nu),y2:y1,stroke:'#6e6e6e','stroke-dasharray':'5 4','stroke-width':1.4},ch);
mk('line',{x1:x0,y1:Y(D.threshold),x2:x1,y2:Y(D.threshold),stroke:'#4d4d4d','stroke-width':1.6},ch);
var line=mk('path',{fill:'none',stroke:LINE,'stroke-width':2.2,'stroke-linejoin':'round'},ch),dd=mk('g',{'class':'pf-dd',opacity:0},ch);
if(D.alarm&&D.alarm>D.nu){var by=y1-22,bx0=X(D.nu),bx1=X(D.alarm);mk('path',{d:'M'+bx0+' '+(by-7)+'V'+by+'H'+bx1+'V'+(by-7),fill:'none',stroke:'#d62728','stroke-width':1.8},dd);mk('text',{x:Math.max(x0+70,Math.min(x1-70,(bx0+bx1)/2)),y:by-9,'text-anchor':'middle','class':'dl'},dd).textContent='detection delay';}
var cur=mk('circle',{r:4.5,fill:LINE,'class':'pf-cur'},ch),starG=mk('g',{},ch),star=mk('path',{fill:'#ffa500','class':'pf-star',d:(function(){var s='',k,a,r;for(k=0;k<10;k++){a=-Math.PI/2+k*Math.PI/5;r=k%2?5:12;s+=(k?'L':'M')+(r*Math.cos(a)).toFixed(2)+' '+(r*Math.sin(a)).toFixed(2);}return s+'Z';})()},starG);
if(D.alarm)starG.setAttribute('transform','translate('+X(D.alarm)+','+Y(D.stat[D.alarm])+')');
mk('rect',{x:x0,y:y0,width:x1-x0,height:y1-y0,fill:'none',stroke:'#000','stroke-width':1.3},ch);
var lg=mk('g',{},ch);mk('rect',{x:x0+10,y:y0+10,width:226,height:56,fill:'#fff',stroke:'#cfcfcf',rx:3},lg);mk('line',{x1:x0+20,y1:y0+27,x2:x0+56,y2:y0+27,stroke:'#6e6e6e','stroke-dasharray':'5 4','stroke-width':1.4},lg);mk('text',{x:x0+66,y:y0+32,'class':'lg'},lg).textContent='Change Point';mk('line',{x1:x0+20,y1:y0+49,x2:x0+56,y2:y0+49,stroke:'#4d4d4d','stroke-width':1.6},lg);mk('text',{x:x0+66,y:y0+54,'class':'lg'},lg).textContent='Detection Threshold';
mk('text',{x:(x0+x1)/2,y:400,'text-anchor':'middle','class':'al'},ch).textContent='Time step';
mk('text',{x:20,y:(y0+y1)/2,'text-anchor':'middle','class':'al',transform:'rotate(-90 20 '+(y0+y1)/2+')'},ch).textContent='System-level Statistics';
var hit=mk('rect',{x:x0,y:y0,width:x1-x0,height:y1-y0,fill:'transparent','class':'pf-hit'},ch),drag=false,fromX=function(e){var r=hit.getBoundingClientRect();return Math.round((e.clientX-r.left)/r.width*xm);};
hit.addEventListener('pointerdown',function(e){if(editing)return;drag=true;try{hit.setPointerCapture(e.pointerId);}catch(_){ }scrub(fromX(e));e.preventDefault();});
hit.addEventListener('pointermove',function(e){if(drag)scrub(fromX(e));});
['pointerup','pointercancel'].forEach(function(n){hit.addEventListener(n,function(){drag=false;unscrub();});});
function steps(n){var d='M'+X(0).toFixed(1)+' '+Y(D.stat[0]).toFixed(1);for(var t=1;t<=n;t++)d+='H'+X(t).toFixed(1)+'V'+Y(D.stat[t]).toFixed(1);return d;}
V={L:L,uavs:uavs,draw:function(t){
abn.forEach(function(r){r.setAttribute('opacity',editing?0.55:(t>=D.nu?1:0));});clear(L.under);clear(L.over);clear(L.tail);
for(var n=0;n<N;n++){var p=rc(D.pos[t][n]);place(uavs[n],p,C);if(editing)continue;
for(var k=Math.max(1,t-TAIL+1);k<=t;k++){var a=rc(D.pos[k-1][n]),b=rc(D.pos[k][n]);if(a[0]==b[0]&&a[1]==b[1])continue;mk('line',{x1:a[1]*C+C/2,y1:a[0]*C+C/2,x2:b[1]*C+C/2,y2:b[0]*C+C/2,stroke:BLUE,'stroke-width':3,'stroke-linecap':'round',opacity:(0.08+0.3*(k-(t-TAIL))/TAIL).toFixed(2)},L.tail);}
if(t<T){arrow(L,svg,C,p,rc(D.pos[t+1][n]),'b');dot(L,C,rc(D.pos[t+1][n]));}}
line.setAttribute('d',editing?'':steps(t));cur.setAttribute('cx',X(t));cur.setAttribute('cy',Y(D.stat[t]));cur.setAttribute('opacity',editing?0:1);
var al=!editing&&D.alarm&&t>=D.alarm;star.classList.toggle('on',!!al);dd.setAttribute('opacity',al?1:0);}};}
function status(t){var s,n=D.anom.length,w=n==1?'An anomaly occurred at one location':('Anomalies occurred at '+n+' locations');
if(editing)s='Press Run to start.';
else if(D.alarm&&t>=D.alarm)s=D.alarm<D.nu||!n?'False alarm at time step '+D.alarm+': the threshold was exceeded before any anomaly occurred.':'Alarm triggered at time step '+D.alarm+', '+(D.alarm-D.nu)+' step'+(D.alarm-D.nu==1?'':'s')+' after the anomalies occurred.'+(t>D.alarm?' The run continues to show the UAVs focusing on the anomalies.':'');
else if(t<D.nu||!n)s='No anomaly yet. The fleet keeps covering the region.';
else s=w+' '+(t-D.nu)+' step'+(t-D.nu==1?'':'s')+' ago. The statistic increases as UAVs revisit '+(n==1?'it':'them')+'.';
if(!editing&&!D.alarm&&t>=D.T)s='No alarm within '+D.T+' time steps.';
if(q('rp-status').textContent!==s)q('rp-status').textContent=s;}
function draw(t){t=Math.max(0,Math.min(D.T,t));now=t;range.max=D.T;range.value=t;q('rp-t').textContent=t;V.draw(t);status(t);q('rp-step').textContent=t+' / '+D.T;
var m='';if(!editing&&D.vis){m=(t<D.nu||!D.anom.length)?'Locations visited so far: '+D.vis[t]+' of '+K:'UAVs on anomalies: '+D.on[t]+' of '+Math.min(D.N,D.anom.length);}q('rp-m').textContent=m;q('rp-rt').textContent=(!editing&&D.ms&&t>=1&&D.ms[t]!=null)?'Decision time this step: '+D.ms[t].toFixed(1)+' ms (one CPU core)':'';}
function glide(){if(now>=D.T||RM)return;for(var n=0;n<D.N;n++)place(V.uavs[n],rc(D.pos[now+1][n]),C);}
function stop(){if(timer){clearInterval(timer);timer=null;}if(mv){clearTimeout(mv);mv=null;}el.classList.remove('playing');play.textContent=now>=D.T?'Replay':'Play';draw(now);}
function tick(){if(now>=D.T){stop();return;}draw(now+1);if(now>=D.T){stop();return;}mv=setTimeout(glide,HOLD);}
function start(){if(editing)return;if(now>=D.T)draw(0);STEP=Math.max(200,Math.min(560,Math.round(42000/Math.max(1,D.T))));HOLD=Math.round(STEP*0.26);el.style.setProperty('--gl',Math.round(STEP*0.62)+'ms');el.classList.add('playing');play.textContent='Pause';mv=setTimeout(glide,HOLD);timer=setInterval(tick,STEP);}
function scrub(t){if(timer)stop();el.classList.add('scrub');draw(t);play.textContent=now>=D.T?'Replay':'Play';}
function unscrub(){el.classList.remove('scrub');}
play.addEventListener('click',function(){timer?stop():start();});
range.addEventListener('input',function(){if(!editing)scrub(+range.value);});range.addEventListener('change',unscrub);range.addEventListener('pointerup',unscrub);
/* an episode as recorded or simulated: full statistic path; the threshold only marks where the alarm falls */
function show(r,auto){raw=r;var H=thr(r.N,st.arl0),al=null,t;if(r.al>0)al=r.al;else for(t=1;t<r.stat.length;t++)if(r.stat[t]>=H){al=t;break;}
D={N:r.N,nu:r.nu,anom:r.anom,pos:r.pos,stat:r.stat,ms:r.ms||null,threshold:H,alarm:al,T:r.stat.length-1};var sn={},vc=0;D.vis=[];D.on=[];for(t=0;t<r.pos.length;t++){var c=0;r.pos[t].forEach(function(k){if(!sn[k]){sn[k]=1;vc++;}if(r.anom.indexOf(k)>=0)c++;});D.vis.push(vc);D.on.push(c);}
editing=false;el.classList.remove('editing');build();draw(0);note();play.disabled=false;range.disabled=false;if(auto&&!RM)start();}
function note(){var m=META[st.N],a=st.arl0;q('rp-note').innerHTML=(raw&&raw.rec?'Recorded run of the learned policy. ':(raw?'Run of the learned policy, computed on the demo server. ':''))+'Detection threshold '+thr(st.N,a).toFixed(2)+', set for ARL<sub>0</sub> = '+a+' with '+st.N+' UAVs.';}
/* settings and runs: the policy runs on a demo server and only the trajectory comes back; recorded runs are the fallback */
var API='https://nixsummer-dispatch-demo.hf.space',MAXC=10,runb=q('pc-run'),KEYS=['N','shift','nu','A','lay'];
function diag(N){var s=[],i,r;for(i=0;i<N;i++){r=N>1?Math.floor(i*(G-1)/(N-1)+1e-9):0;s.push(r*G+r);}return s;}
function seg(k){return el.querySelector('.pc-seg[data-k="'+k+'"]');}
function setSeg(k,v){[].forEach.call(seg(k).children,function(b){b.setAttribute('aria-pressed',b.getAttribute('data-v')==String(v)?'true':'false');});}
function counts(){q('pc-cc').textContent='Anomalies: '+st.cells.length;}
function sync(){counts();setSeg('N',st.N);q('pc-nu').value=st.nu;q('pc-nuv').textContent='time step '+st.nu;q('pc-sh').value=st.shift;q('pc-sh').setAttribute('aria-valuetext',st.shift<2.67?'small':(st.shift<3.34?'medium':'large'));}
/* edit view: the starting layout and the abnormal locations, before a run */
function edit(){counts();if(timer)stop();editing=true;el.classList.add('editing');raw=null;D={N:st.N,nu:st.nu,anom:st.cells.slice(),pos:[st.start.slice()],stat:[0],threshold:thr(st.N,st.arl0),alarm:null,T:0,vis:null};build();draw(0);play.disabled=true;range.disabled=true;note();msg.textContent='';runb.textContent='Run';}
/* setup gestures: drag a UAV to move its start position, click a location to mark or clear it as abnormal */
var nudged=false,dg=null,W0=G*C;
function at(e){var r=svg.getBoundingClientRect(),x=(e.clientX-r.left)/r.width*504-2,y=(e.clientY-r.top)/r.height*504-2;return {x:x,y:y,k:(x<0||y<0||x>=W0||y>=W0)?-1:Math.floor(y/C)*G+Math.floor(x/C)};}
function mark(name,k,at2){var m=V[name];if(!m){m=V[name]=mk('rect',at2,name=='hov'?V.L.cells:V.L.under);}if(k<0){m.setAttribute('opacity',0);return;}m.setAttribute('x',(k%G)*C+(name=='hov'?0:3));m.setAttribute('y',Math.floor(k/G)*C+(name=='hov'?0:3));m.setAttribute('opacity',1);}
function hover(k){mark('hov',k,{width:C,height:C,fill:ABN,'fill-opacity':0.3,opacity:0,'pointer-events':'none'});}
function drop(k){mark('drop',k,{width:C-6,height:C-6,rx:4,fill:'none',stroke:BLUE,'stroke-width':3,'stroke-dasharray':'7 5',opacity:0,'pointer-events':'none'});}
svg.addEventListener('pointerdown',function(e){if(busy||e.button>0)return;var p=at(e);if(p.k<0)return;
if(!editing){edit();msg.textContent='';dg=null;return;}
var i=st.start.indexOf(p.k);
if(i>=0){dg={i:i,to:p.k,ox:p.x-(p.k%G)*C,oy:p.y-Math.floor(p.k/G)*C};try{svg.setPointerCapture(e.pointerId);}catch(_){ }el.classList.add('dragging');V.uavs[i].classList.remove('nudge');V.uavs[i].classList.add('pk');V.L.icons.appendChild(V.uavs[i]);hover(-1);drop(p.k);e.preventDefault();}
else dg={i:-1,k:p.k,x:e.clientX,y:e.clientY};});
svg.addEventListener('pointermove',function(e){if(!editing||busy)return;var p=at(e);
if(dg&&dg.i>=0){var x=Math.max(0,Math.min(W0-C,p.x-dg.ox)),y=Math.max(0,Math.min(W0-C,p.y-dg.oy)),k=Math.floor((y+C/2)/C)*G+Math.floor((x+C/2)/C),o=st.start.indexOf(k);
V.uavs[dg.i].style.transform='translate('+x+'px,'+y+'px)';if(o<0||o==dg.i){dg.to=k;drop(k);}e.preventDefault();return;}
if(e.pointerType=='mouse')hover(p.k>=0&&st.start.indexOf(p.k)<0&&st.cells.indexOf(p.k)<0&&st.cells.length<MAXC?p.k:-1);});
function endDrag(e,cancel){if(!dg)return;var d=dg,m='';dg=null;el.classList.remove('dragging');if(!editing)return;
if(d.i>=0){if(!cancel)st.start[d.i]=d.to;}
else if(!cancel){var p=at(e);if(p.k==d.k&&Math.abs(e.clientX-d.x)<9&&Math.abs(e.clientY-d.y)<9){var i=st.cells.indexOf(d.k);if(i>=0)st.cells.splice(i,1);else if(st.cells.length>=MAXC)m='This demo takes up to '+MAXC+' anomalies. Click one to clear it first.';else st.cells.push(d.k);}else return;}
edit();msg.textContent=m;}
svg.addEventListener('pointerup',function(e){endDrag(e,false);});svg.addEventListener('pointercancel',function(e){endDrag(e,true);});
svg.addEventListener('pointerleave',function(){if(V&&V.hov)hover(-1);});
/* a finger on a UAV drags it; a finger anywhere else on the grid scrolls the page */
svg.addEventListener('touchstart',function(e){if(editing&&!busy&&e.target.closest&&e.target.closest('.pf-u'))e.preventDefault();},{passive:false});
el.querySelector('.pc').addEventListener('click',function(e){var b=e.target.closest('.pc-seg button');if(!b||busy)return;st.N=+b.getAttribute('data-v');st.start=diag(st.N);sync();edit();});
q('pc-nu').addEventListener('input',function(){st.nu=+this.value;sync();if(!busy)edit();});
q('pc-sh').addEventListener('input',function(){st.shift=+this.value;sync();if(!busy)edit();});
q('pc-rand').addEventListener('click',function(){if(busy)return;var s=[];while(s.length<st.N){var k=Math.floor(Math.random()*K);if(s.indexOf(k)<0)s.push(k);}st.start=s;edit();});
/* random abnormal locations: spread apart, or one connected group; the count stays as it is */
function nbr(k){var r=Math.floor(k/G),c=k%G,o=[];if(r>0)o.push(k-G);if(r<G-1)o.push(k+G);if(c>0)o.push(k-1);if(c<G-1)o.push(k+1);return o;}
function scatter(n){var s=[],tries=0;while(s.length<n&&tries<4000){tries++;var k=Math.floor(Math.random()*K);if(s.indexOf(k)>=0)continue;if(tries<3000&&s.some(function(x){return Math.abs(Math.floor(x/G)-Math.floor(k/G))<=1&&Math.abs(x%G-k%G)<=1;}))continue;s.push(k);}return s;}
function cluster(n){var s=[Math.floor(Math.random()*K)];while(s.length<n){var f=[];s.forEach(function(x){nbr(x).forEach(function(y){if(s.indexOf(y)<0&&f.indexOf(y)<0)f.push(y);});});s.push(f[Math.floor(Math.random()*f.length)]);}return s;}
q('pc-scat').addEventListener('click',function(){if(busy)return;st.cells=scatter(st.cells.length||5);edit();});
q('pc-clus').addEventListener('click',function(){if(busy)return;st.cells=cluster(st.cells.length||5);edit();});
/* recorded runs, used when the server cannot be reached */
function has(c){var b=IDX.avail[c.N+'_'+c.shift];if(!b)return false;var i=(IDX.anoms.indexOf(+c.A)*IDX.nus.length+IDX.nus.indexOf(+c.nu))*IDX.layouts.length+IDX.layouts.indexOf(c.lay);return i>=0&&b.charAt(i)=='1';}
var ALL=(function(){var o=[];IDX.Ns.forEach(function(N){IDX.shifts.forEach(function(s){IDX.anoms.forEach(function(A){IDX.nus.forEach(function(nu){IDX.layouts.forEach(function(l){var c={N:N,shift:s,nu:nu,A:A,lay:l};if(has(c))o.push(c);});});});});});return o;})(),W={N:1000,shift:60,A:20,nu:6,lay:1};
function near(c,k){var best=null,bd=1e9;ALL.forEach(function(o){if(String(o[k])!=String(c[k]))return;var d=0;KEYS.forEach(function(x){if(String(o[x])!=String(c[x]))d+=W[x]*(1+(x=='lay'?0:Math.abs(o[x]-c[x])/100));});if(d<bd){bd=d;best=o;}});return best;}
function unpack(f,key){var r=f.runs[key],N=f.N,p=r.p,T=p.length/(2*N)-1,pos=[],t,n;for(t=0;t<=T;t++){var row=[];for(n=0;n<N;n++)row.push(+p.substr((t*N+n)*2,2));pos.push(row);}
return {N:N,nu:+key.split('_')[1],anom:r.anom,pos:pos,stat:r.s.map(function(v){return v/10;}),al:r.al,rec:true};}
function file(N,s){var k=N+'_'+s;if(!files[k]){files[k]=fetch('data/demo/runs/n'+N+'_s'+s+'.json').then(function(r){if(!r.ok)throw new Error('load');return r.json();});files[k].catch(function(){files[k]=null;});}return files[k];}
function done(){busy=false;runb.disabled=false;q('pc-reset').disabled=false;runb.textContent='Run again';}
function fallback(){var DOWN='The demo server could not be reached. ',n=st.cells.length,c={N:st.N,shift:Math.max(2,Math.min(4,Math.round(st.shift))),nu:Math.max(10,Math.min(60,Math.round(st.nu/10)*10)),A:IDX.anoms.reduce(function(a,b){return Math.abs(b-n)<Math.abs(a-n)?b:a;}),lay:'scatter1'},o=near(c,'N');
if(!o){done();msg.textContent=DOWN+'Try again in a minute.';return;}
file(o.N,o.shift).then(function(f){var r=unpack(f,o.A+'_'+o.nu+'_'+o.lay);done();st.cells=r.anom.slice();st.start=r.pos[0].slice();st.nu=r.nu;st.shift=o.shift;sync();show(r,true);if(RM)draw(D.T);msg.textContent=DOWN+'Showing a recorded run for a similar setting.';})
.catch(function(){done();msg.textContent=DOWN+'Try again in a minute.';});}
function post(){return fetch(API+'/run',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({N:st.N,shift:st.shift,nu:st.nu,cells:st.cells,start:st.start})}).then(function(r){return r.json().then(function(j){if(!r.ok){var e=new Error((j&&j.error)||'server');e.user=(r.status==400||r.status==429)&&!!(j&&j.error);throw e;}return j;});});}
/* a sleeping server answers with an error page and is polled until it is up; no answer at all means it cannot be reached from here */
function wake(until){return fetch(API+'/').then(function(r){if(r.ok)return r.json();if(Date.now()>until)throw new Error('down');return new Promise(function(res){setTimeout(res,4000);}).then(function(){return wake(until);});},function(){throw new Error('down');});}
function run(){if(busy)return;if(!st.cells.length){msg.textContent='Place at least one anomaly on the grid.';return;}if(timer)stop();busy=true;runb.disabled=true;q('pc-reset').disabled=true;msg.textContent='Running DispatchPPO on Hugging Face ...';
var slow=setTimeout(function(){msg.textContent='Starting the demo server. This can take up to a minute ...';},7000);
post().catch(function(e){if(e.user)throw e;return wake(Date.now()+75000).then(post);})
.then(function(j){clearTimeout(slow);done();msg.textContent='';show({N:j.N,nu:j.nu,anom:j.anom,pos:j.pos,stat:j.stat,al:j.al,ms:j.ms},true);if(RM)draw(D.T);})
.catch(function(e){clearTimeout(slow);if(e&&e.user){done();runb.textContent='Run';msg.textContent=e.message;return;}fallback();});}
runb.addEventListener('click',run);var rsb=q('pc-reset');rsb.addEventListener('click',function(){if(busy)return;st.N=REC.N;st.shift=REC.shift;st.nu=REC.nu;st.cells=REC.anom.slice();st.start=REC.pos[0].slice();sync();edit();});
sync();edit();
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){if(!nudged&&!RM&&editing&&V.uavs.length){nudged=true;V.uavs[V.uavs.length>2?2:0].classList.add('nudge');}}else if(timer){stop();}});},{threshold:0.35});io.observe(el.querySelector('.pf-panel'));}
document.addEventListener('visibilitychange',function(){if(document.hidden&&timer)stop();});
})();
/* ---- DispatchNet decoder, illustrated: the reader places UAVs and anomalies; the grid and a decoder strip drawn like the paper figure play one move together ---- */
function decoder(id,cfg){var el=document.getElementById(id);if(!el)return;var G=cfg.G,M=cfg.N,C=50,W=G*C,SW=11+153*M,RED='#d62728',DARK='#4f4f4f',OFF='#c4c4c4',NAME=['up-left','up','up-right','left','stay','right','down-left','down','down-right'],GLY=['↖','↑','↗','←','•','→','↙','↓','↘'];
var q=function(r){return el.querySelector('[data-r="'+r+'"]');},svg=q('grid'),st=q('strip'),play=q('play'),stat=q('status'),msg=q('msg'),mkb=q('mask'),csb=q('cases'),X=[],i;for(i=0;i<M;i++)X.push(82+153*i);
svg.setAttribute('viewBox','-2 -2 '+(W+4)+' '+(W+4));st.setAttribute('viewBox','0 0 '+SW+' 396');
var pos=cfg.pos.map(function(p){return p.slice();}),anom=cfg.anom.map(function(p){return p.slice();}),mask=1,timers=[],running=false,moved=false,tally=[[0,0],[0,0]],drag=null,dragged=false,L,uavs,shade,marks,cols,pass,steps=[],si=0,fast=false,left=0,frozen=false,nxb=q('next'),qkb=q('quick');
function later(f,ms){timers.push(setTimeout(f,RM?Math.round(ms*0.55):ms));}
function cell(p,a){return [p[0]+Math.floor(a/3)-1,p[1]+a%3-1];}
function same(a,b){return a[0]==b[0]&&a[1]==b[1];}
function inside(c){return c[0]>=0&&c[0]<G&&c[1]>=0&&c[1]<G;}
function txt(p,x,y,s,c){var t=mk('text',{x:x,y:y,'class':c||''},p);t.textContent=s;return t;}
/* the 9 preference bars of one UAV; a removed move is drawn dark, as in the figure */
function bars(g,x,base,pref,gone,pick){clear(g);for(var a=0;a<9;a++){var v=pref[a]||0,bx=x-60.5+a*14,h=Math.max(3,v*cfg.sc),off=gone&&gone[a]&&v>=1,r=Math.round(v);mk('rect',{x:bx,y:base-h,width:9,height:h,fill:off?DARK:(a===pick?'#174f96':BLUE),opacity:v>=1?1:0.35},g);
if(cfg.labels&&r>=1)txt(g,bx+4.5,base-h-4,r+'%','dm-p'+(off?' off':''));txt(g,bx+4.5,base+13,GLY[a],'dm-g');}mk('line',{x1:x-65,y1:base,x2:x+65,y2:base,stroke:'#111','stroke-width':1.2},g);}
function mgrid(g,x,y,gone){clear(g);for(var a=0;a<9;a++)mk('rect',{x:x-24+(a%3)*16,y:y+Math.floor(a/3)*16,width:16,height:16,fill:gone&&gone[a]?(gone[a]==1?OFF:DARK):'#fff',stroke:'#8a8a8a','stroke-width':1},g);}
function strip(){clear(st);var d=mk('defs',{},st),m=mk('marker',{id:id+'-ah',viewBox:'0 0 10 10',refX:8,refY:5,markerWidth:6,markerHeight:6,orient:'auto'},d);mk('path',{d:'M1 1L9 5L1 9',fill:'none',stroke:'#8a8a8a','stroke-width':1.8},m);
mk('rect',{x:0,y:0,width:SW,height:396,fill:'#fff'},st);txt(st,8,13,'Dispatch Action','dm-c b');mk('rect',{x:6,y:20,width:SW-12,height:28,rx:9,fill:'none',stroke:'#2f6fb0','stroke-width':1.6,'stroke-dasharray':'5 4'},st);
mk('rect',{x:6,y:58,width:SW-12,height:176,rx:8,fill:'#ececec'},st);pass=mk('g',{},st);txt(st,14,75,'Collision-Aware Masking','dm-c h');txt(st,8,272,'Scores from the decoder','dm-c');
cols=X.map(function(x,k){var g=mk('g',{'class':'dm-col'},st);txt(g,x,253,'+','dm-plus');var o={g:g,act:txt(g,x,39,'','dm-a'),after:mk('g',{},g),mask:mk('g',{},g),pref:mk('g',{},g),lab:txt(g,x,390,'UAV '+(k+1),'dm-u')};mgrid(o.mask,x,178);return o;});}
function idle(keep){timers.forEach(clearTimeout);timers=[];running=false;frozen=false;stat.classList.remove('hit');if(!keep){fast=false;left=0;steps=[];si=0;upd();}clear(svg);L=gridSvg(svg,G,C);
anom.forEach(function(p){mk('rect',{x:p[1]*C,y:p[0]*C,width:C,height:C,fill:ABN},L.cells);});shade=mk('g',{},L.cells);
uavs=pos.map(function(p,k){var g=icon(L,svg,C);mk('circle',{cx:C-9,cy:10,r:9,fill:'#111'},g);txt(g,C-9,14.5,k+1,'dm-n');place(g,p,C);return g;});marks=mk('g',{},svg);
strip();el.classList.toggle('nomask',!mask);el.classList.remove('run');el.classList.add('editing');
if(!keep){play.textContent=moved?'Next move':'Play';stat.textContent=cfg.hint;}
if(csb)[].forEach.call(csb.children,function(b,i){b.setAttribute('aria-pressed',i===cfg.ci?'true':'false');});[].forEach.call(mkb.children,function(b){b.setAttribute('aria-pressed',(+b.getAttribute('data-v'))==mask?'true':'false');});}
function changed(){moved=false;cfg.ci=-1;idle();}
/* rows: one per UAV in decoding order {u, p, pref[9] in percent, gone[9] (1 off the grid, 2 reserved), best, top} */
function animate(rows){idle(true);running=true;el.classList.remove('editing');el.classList.add('run');play.textContent=fast?'Play':'Next UAV';var dest=[],STEP=3300;steps=[];si=0;
rows.forEach(function(r,k){cols[k].lab.textContent='UAV '+(r.u+1);});
rows.forEach(function(r,k){var o=cols[k],x=X[k],t0=k*STEP,p=r.p,nres=0,noff=0,a;for(a=0;a<9;a++){if(r.gone[a]==2)nres++;if(r.gone[a]==1)noff++;}dest[r.u]=cell(p,r.best);
steps.push({k:k,t:t0,first:true,f:function(){cols.forEach(function(c,i){c.g.classList.toggle('on',i==k);});clear(shade);clear(marks);mk('rect',{x:p[1]*C-C+2,y:p[0]*C-C+2,width:3*C-4,height:3*C-4,rx:6,'class':'dm-ring'},marks);
for(a=0;a<9;a++){var v=r.pref[a]||0,c=cell(p,a);if(v>=1&&inside(c))mk('rect',{x:c[1]*C,y:c[0]*C,width:C,height:C,fill:BLUE,opacity:Math.min(0.9,0.1+v/100*cfg.sc*1.1).toFixed(2),'class':'dm-sh'},shade);}
bars(o.pref,x,348,r.pref);stat.textContent='UAV '+(r.u+1)+': '+cfg.pre;}});
steps.push({k:k,t:t0+850,f:function(){mgrid(o.mask,x,178,r.gone);for(a=0;a<9;a++)if(r.gone[a]==2){var c=cell(p,a);mk('rect',{x:c[1]*C,y:c[0]*C,width:C,height:C,fill:DARK,opacity:0.5,'class':'dm-sh'},shade);}
stat.textContent=(!mask?'Without DispatchNet, no location is reserved.':(nres?'The mask reserves '+nres+' location'+(nres==1?'':'s')+' near UAV '+(r.u+1)+' (dark).':'No location near UAV '+(r.u+1)+' is reserved.'))+(noff?' Moves outside the grid are masked (grey).':'');}});
steps.push({k:k,t:t0+1650,f:function(){bars(o.after,x,150,r.pref,r.gone);}});
steps.push({k:k,t:t0+2300,f:function(){o.act.textContent=GLY[r.best]+' '+NAME[r.best];bars(o.after,x,150,r.pref,r.gone,r.best);arrow(L,svg,C,p,dest[r.u],'b');dot(L,C,dest[r.u]);
if(mask&&k<M-1)mk('path',{d:'M'+(x+66)+' 48C'+(x+86)+' 48 '+(x+68)+' 202 '+(X[k+1]-30)+' 202',fill:'none',stroke:'#8a8a8a','stroke-width':1.8,'marker-end':'url(#'+id+'-ah)','class':'pf-ar'},pass);
stat.textContent='The move of UAV '+(r.u+1)+(mask?' is sampled from the masked distribution: ':' is sampled without the mask: ')+NAME[r.best]+'.';}});});
steps.push({k:M,t:M*STEP,f:function(){clear(shade);clear(marks);clear(L.under);clear(L.over);cols.forEach(function(c){c.g.classList.add('on');});el.classList.remove('run');var hit=null,i,j;
for(i=0;i<M;i++){place(uavs[i],dest[i],C);for(j=i+1;j<M;j++)if(same(dest[i],dest[j])||(same(dest[i],pos[j])&&same(dest[j],pos[i])))hit=[i,j];}
var t=tally[mask];t[0]++;if(hit)t[1]++;msg.innerHTML=['Without DispatchNet','With DispatchNet'].map(function(n,i){var c=tally[i],k=c[1]+' collision'+(c[1]==1?'':'s');return c[0]?n+': '+c[0]+' move'+(c[0]==1?'':'s')+', '+(c[1]?'<b class="dm-red">'+k+'</b>':k):'';}).filter(String).reverse().join('. ')+'.';
if(!hit){pos=dest.map(function(d){return d.slice();});moved=true;running=false;el.classList.add('editing');play.textContent='Next move';stat.textContent=mask?'All '+M+' UAVs move together. The joint move is collision-free.':'No collision this time, but the joint move is not collision-free by construction.';if(fast&&--left>0)later(quick,650);else{fast=false;upd();}return;}fast=false;left=0;upd();
frozen=true;upd();cols[hit[0]].act.classList.add('hit');cols[hit[1]].act.classList.add('hit');stat.classList.add('hit');later(function(){var d=dest[hit[0]],lx;mk('rect',{x:d[1]*C+3,y:d[0]*C+3,width:C-6,height:C-6,rx:4,'class':'dm-hit'},marks);if(!same(dest[hit[0]],dest[hit[1]])){var d2=dest[hit[1]];mk('rect',{x:d2[1]*C+3,y:d2[0]*C+3,width:C-6,height:C-6,rx:4,'class':'dm-hit'},marks);}lx=Math.max(0,Math.min(W-58,d[1]*C+C/2-29));mk('rect',{x:lx,y:d[0]*C+C-17,width:58,height:15,rx:7.5,'class':'dm-tag'},marks);txt(marks,lx+29,d[0]*C+C-6,'Collision','dm-tagt');},560);
play.textContent='Undo the collision';stat.textContent='Without DispatchNet, UAV '+(hit[0]+1)+' and UAV '+(hit[1]+1)+(same(dest[hit[0]],dest[hit[1]])?' move to the same location':' swap positions')+': a collision.';}});
if(fast){while(steps[si].k<M)steps[si++].f();cols.forEach(function(c){c.g.classList.add('on');});clear(shade);clear(marks);sched(450);}else sched(0);upd();}
/* the steps of one move run on a schedule; Next UAV finishes the UAV being decoded and starts the next one at once */
function sched(d){var t0=steps[si].t;steps.slice(si).forEach(function(s){later(function(){si++;s.f();upd();},s.t-t0+d);});}
function skip(){timers.forEach(clearTimeout);timers=[];if(steps[si].k>=M){steps[si++].f();upd();return;}if(!steps[si].first){var k=steps[si].k;while(steps[si].k==k)steps[si++].f();}sched(steps[si].k>=M?500:0);upd();}
function quick(){if(drag)return;fast=true;animate(cfg.rows(pos,mask));}
/* a collision stays on screen until the reader undoes it */
function undo(){frozen=false;clear(marks);stat.classList.remove('hit');uavs.forEach(function(g,i){place(g,pos[i],C);});upd();later(function(){idle();},600);}
function upd(){if(nxb)nxb.disabled=!(running&&!fast&&steps[si]&&steps[si].k<M);if(qkb)qkb.disabled=fast||frozen;if(running&&!fast&&steps[si]&&steps[si].k>=M)play.textContent='Move the UAVs';}

function run(){if(drag)return;fast=false;left=0;animate(cfg.rows(pos,mask));}
play.addEventListener('click',function(){if(frozen)undo();else if(running&&!fast&&steps[si])skip();else run();});
if(nxb)nxb.addEventListener('click',skip);if(qkb)qkb.addEventListener('click',function(){left=10;quick();});var ci0=cfg.ci,rs=q('reset');if(rs)rs.addEventListener('click',function(){pos=cfg.pos.map(function(p){return p.slice();});anom=cfg.anom.map(function(p){return p.slice();});mask=1;moved=false;tally=[[0,0],[0,0]];msg.textContent='';cfg.ci=ci0;idle();});
if(csb)cfg.cases.forEach(function(c,i){var b=document.createElement('button');b.type='button';b.textContent=c.name;b.addEventListener('click',function(){pos=c.pos.map(function(p){return p.slice();});anom=c.anom.map(function(p){return p.slice();});changed();cfg.ci=i;idle();});csb.appendChild(b);});
mkb.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;mask=+b.getAttribute('data-v');idle();});
/* the reader's layout: drag a UAV to another location, click a location to add or remove an anomaly */
function at(e){var r=svg.getBoundingClientRect();return [((e.clientY-r.top)/r.height*(W+4)-2)/C,((e.clientX-r.left)/r.width*(W+4)-2)/C];}
svg.addEventListener('pointerdown',function(e){if(frozen){undo();return;}if(running||e.button>0)return;var g=e.target.closest&&e.target.closest('.pf-u'),k=g?uavs.indexOf(g):-1;if(k<0)return;var p0=at(e);drag={k:k,moved:false,o:[p0[0]-pos[k][0],p0[1]-pos[k][1]]};try{svg.setPointerCapture(e.pointerId);}catch(_){ }el.classList.add('dragging');e.preventDefault();});
svg.addEventListener('pointermove',function(e){if(!drag)return;var p=at(e);drag.moved=true;uavs[drag.k].style.transform='translate('+((p[1]-drag.o[1])*C).toFixed(1)+'px,'+((p[0]-drag.o[0])*C).toFixed(1)+'px)';});
function drop(e,cancel){if(!drag)return;var p=at(e),c=[Math.floor(p[0]-drag.o[0]+0.5),Math.floor(p[1]-drag.o[1]+0.5)],k=drag.k,ok=!cancel&&drag.moved&&inside(c)&&!pos.some(function(o,i){return i!=k&&same(o,c);});el.classList.remove('dragging');dragged=true;setTimeout(function(){dragged=false;},250);drag=null;
if(ok&&!same(pos[k],c)){pos[k]=c;changed();}else place(uavs[k],pos[k],C);}
svg.addEventListener('pointerup',function(e){drop(e,false);});svg.addEventListener('pointercancel',function(e){drop(e,true);});
svg.addEventListener('click',function(e){if(!cfg.maxA||running||dragged||(e.target.closest&&e.target.closest('.pf-u')))return;var p=at(e),c=[Math.floor(p[0]),Math.floor(p[1])],i;if(!inside(c))return;
for(i=0;i<anom.length;i++)if(same(anom[i],c)){if(anom.length>1){anom.splice(i,1);changed();}else stat.textContent='Keep at least one anomaly on the grid.';return;}
if(anom.length>=cfg.maxA){stat.textContent='At most '+cfg.maxA+' anomalies in this illustration.';return;}anom.push(c);changed();});
document.addEventListener('visibilitychange',function(){if(document.hidden&&running&&!frozen)idle();});
idle();}
/* preferences of an untrained DispatchNet (random weights), stored for every layout of 3 UAVs on the 3x3 grid: 9 values per UAV, UAVs in the order of their locations */
(function(){var e=document.getElementById('dm-tab');if(!e)return;var T=JSON.parse(e.textContent),G=T.G,N=T.N,K=G*G,bin=atob(T.p),index={},n=0,a,b,c;
for(a=0;a<K;a++)for(b=a+1;b<K;b++)for(c=b+1;c<K;c++)index[a+','+b+','+c]=n++;
function rows(pos,mask){var id=pos.map(function(p){return p[0]*G+p[1];}),sorted=id.slice().sort(function(x,y){return x-y;}),base=index[sorted.join(',')]*N*9,out=[],dest=[],k,j;
for(k=0;k<N;k++){var p=pos[k],off=base+sorted.indexOf(id[k])*9,pref={},gone={},sum=0;
for(a=0;a<9;a++){var q=[p[0]+Math.floor(a/3)-1,p[1]+a%3-1];pref[a]=bin.charCodeAt(off+a)/255*100;if(q[0]<0||q[0]>=G||q[1]<0||q[1]>=G){gone[a]=1;continue;}
if(mask&&a!=4){var res=false;for(j=0;j<k;j++)if(dest[j][0]==q[0]&&dest[j][1]==q[1])res=true;for(j=k+1;j<N;j++)if(pos[j][0]==q[0]&&pos[j][1]==q[1])res=true;if(res){gone[a]=2;continue;}}sum+=pref[a];}
var x=Math.random()*sum,best=4;for(a=0;a<9;a++){if(gone[a])continue;x-=pref[a];best=a;if(x<=0)break;}
dest[k]=[p[0]+Math.floor(best/3)-1,p[1]+best%3-1];out.push({u:k,p:p,pref:pref,gone:gone,best:best});}return out;}
decoder('dm',{G:G,N:N,sc:3,labels:false,maxA:0,ci:1,rows:rows,pre:'the decoder scores its 9 local moves.',hint:'Click Play to decode one joint move. During decoding, the same button decodes the next UAV at once.',
cases:[{name:'Far apart',pos:[[0,0],[0,2],[2,1]],anom:[]},{name:'In a row',pos:[[1,0],[1,1],[1,2]],anom:[]},{name:'Crowded',pos:[[1,1],[1,2],[2,1]],anom:[]}],pos:[[1,0],[1,1],[1,2]],anom:[]});})();
/* ---- Robotarium clip: camera with trajectories and statistic drawn beside it, jump buttons and progress bar ---- */
(function(){var el=document.getElementById('rb');if(!el)return;var D=JSON.parse(document.getElementById('rb-data').textContent),v=el.querySelector('video'),q=function(r){return el.querySelector('[data-r="'+r+'"]');},bar=q('bar'),fill=q('fill'),tm=q('time'),bs=[].slice.call(el.querySelectorAll('button[data-t]')),RUN=400,raf=0,INK='#111',GR='#e4e4e4';
function tx(g,x,y,s,a,c){var t=mk('text',{x:x,y:y,'text-anchor':a||'middle','class':c||'rb-tk'},g);t.textContent=s;return t;}
/* trajectories: East 0..3.2 m, North 0..-1.8 m, equal scale as in the camera view */
var T=q('traj'),K=62,TX=function(e){return 76+e*K;},TY=function(n){return 10-n*K;},i,j;
for(i=0;i<=10;i++)mk('line',{x1:TX(i*0.32),y1:TY(0),x2:TX(i*0.32),y2:TY(-1.8),stroke:GR,'stroke-width':0.6},T);
for(i=0;i<=9;i++)mk('line',{x1:TX(0),y1:TY(-i*0.2),x2:TX(3.2),y2:TY(-i*0.2),stroke:GR,'stroke-width':0.6},T);
mk('rect',{x:TX(0),y:TY(0),width:3.2*K,height:1.8*K,fill:'none',stroke:INK,'stroke-width':0.8},T);
[0,0.64,1.28,1.92,2.56,3.2].forEach(function(e){tx(T,TX(e),TY(-1.8)+11,e.toFixed(2));});[0,-0.6,-1.2,-1.8].forEach(function(n){tx(T,TX(0)-4,TY(n)+3.2,n.toFixed(1),'end');});
tx(T,TX(1.6),TY(-1.8)+22,'East (m)','middle','rb-al');var yl=tx(T,TX(0)-30,TY(-0.9),'North (m)','middle','rb-al');yl.setAttribute('transform','rotate(-90 '+(TX(0)-30)+' '+TY(-0.9)+')');
var TR=D.traj.map(function(r){return {q:r.q,path:mk('path',{d:'',fill:'none',stroke:r.c,'stroke-width':0.9,'stroke-dasharray':'1.4 1.4','stroke-linejoin':'round',opacity:0.85},T)};});
var AN=mk('g',{},T);D.anom.forEach(function(p){var x=TX(p[0]),y=TY(p[1]);mk('path',{d:'M'+(x-3.4)+' '+(y-3.4)+'L'+(x+3.4)+' '+(y+3.4)+'M'+(x-3.4)+' '+(y+3.4)+'L'+(x+3.4)+' '+(y-3.4),stroke:'#d62728','stroke-width':1.6,'stroke-linecap':'round'},AN);});
TR.forEach(function(r,n){r.dot=mk('circle',{r:2.4,fill:D.traj[n].c},T);});
function trail(t){var k=Math.min(t/D.dt,D.traj[0].q.length-1),n=Math.floor(k),f=k-n;TR.forEach(function(r){var d='',i,p,x,y;for(i=0;i<=n;i++){p=r.q[i];d+=(i?'L':'M')+TX(p[0]*0.32).toFixed(1)+' '+TY(-p[1]*0.2).toFixed(1);}p=r.q[n];var b=r.q[Math.min(n+1,r.q.length-1)];x=TX((p[0]+(b[0]-p[0])*f)*0.32);y=TY(-(p[1]+(b[1]-p[1])*f)*0.2);r.path.setAttribute('d',d+'L'+x.toFixed(1)+' '+y.toFixed(1));r.dot.setAttribute('cx',x.toFixed(1));r.dot.setAttribute('cy',y.toFixed(1));});}
/* statistic against time */
var S=q('stat'),SX=function(t){return 40+t/RUN*268;},SY=function(h){return 122-h/200*112;};
for(i=0;i<=4;i++){mk('line',{x1:SX(i*100),y1:SY(0),x2:SX(i*100),y2:SY(200),stroke:GR,'stroke-width':0.6},S);tx(S,SX(i*100),SY(0)+11,i*100);mk('line',{x1:SX(0),y1:SY(i*50),x2:SX(RUN),y2:SY(i*50),stroke:GR,'stroke-width':0.6},S);tx(S,SX(0)-4,SY(i*50)+3.2,i*50,'end');}
mk('rect',{x:SX(0),y:SY(200),width:268,height:112,fill:'none',stroke:INK,'stroke-width':0.8},S);
tx(S,SX(200),SY(0)+22,'Time (s)','middle','rb-al');yl=tx(S,12,SY(100),'Statistic','middle','rb-al');yl.setAttribute('transform','rotate(-90 12 '+SY(100)+')');
mk('line',{x1:SX(D.tau),y1:SY(0),x2:SX(D.tau),y2:SY(200),stroke:'#555','stroke-width':0.9,'stroke-dasharray':'3 2.5'},S);tx(S,SX(D.tau)-4,SY(200)+11,'Change point','end','rb-lg');
mk('line',{x1:SX(0),y1:SY(D.H),x2:SX(RUN),y2:SY(D.H),stroke:'#555','stroke-width':0.9},S);tx(S,SX(0)+5,SY(D.H)-4,'Detection threshold','start','rb-lg');
var cp=mk('clipPath',{id:'rb-clip'},S),cr=mk('rect',{x:SX(0)-2,y:0,width:0,height:150},cp),d='';D.stat.forEach(function(p,k){d+=(k?'L':'M')+SX(Math.min(RUN,p[0])).toFixed(1)+' '+SY(Math.min(200,p[1])).toFixed(1);});
mk('path',{d:d,fill:'none',stroke:LINE,'stroke-width':1.5,'stroke-linejoin':'round','clip-path':'url(#rb-clip)'},S);
var star='',a,r;for(i=0;i<10;i++){a=-Math.PI/2+i*Math.PI/5;r=i%2?2.6:6;star+=(i?'L':'M')+(SX(D.alarm)+r*Math.cos(a)).toFixed(1)+' '+(SY(D.H)+r*Math.sin(a)).toFixed(1);}
var ST=mk('path',{d:star+'Z',fill:'#ffa500'},S),tip=mk('circle',{r:2.6,fill:LINE},S);
function val(t){var h=0;for(var k=0;k<D.stat.length&&D.stat[k][0]<=t;k++)h=D.stat[k][1];return h;}
function dur(){return v.duration&&isFinite(v.duration)?v.duration:40;}
function draw(){var f=Math.min(1,v.currentTime/dur()),t=f*RUN,R=Math.round(t),k=t>=D.alarm?2:(t>=D.tau?1:0);fill.style.width=(f*100).toFixed(2)+'%';tm.textContent='t = '+R+' s';bar.setAttribute('aria-valuenow',R);bs.forEach(function(b,n){b.classList.toggle('on',n==k);});
cr.setAttribute('width',(SX(t)-SX(0)+2).toFixed(1));tip.setAttribute('cx',SX(t).toFixed(1));tip.setAttribute('cy',SY(Math.min(200,val(t))).toFixed(1));ST.style.display=t>=D.alarm?'':'none';AN.style.display=t>=D.tau?'':'none';trail(t);}
function loop(){draw();raf=requestAnimationFrame(loop);}
function go(t){v.currentTime=Math.max(0,Math.min(RUN,t))/RUN*dur();draw();var p=v.play();if(p&&p.catch)p.catch(function(){});}
bs.forEach(function(b){b.addEventListener('click',function(){var t=+b.getAttribute('data-t');go(t?t-10:0);});});
bar.addEventListener('click',function(e){var r=bar.getBoundingClientRect();go((e.clientX-r.left)/r.width*RUN);});
bar.addEventListener('keydown',function(e){if(e.key=='ArrowLeft'||e.key=='ArrowRight'){e.preventDefault();go(v.currentTime/dur()*RUN+(e.key=='ArrowRight'?10:-10));}});
v.addEventListener('play',function(){cancelAnimationFrame(raf);loop();});v.addEventListener('pause',function(){cancelAnimationFrame(raf);draw();});v.addEventListener('seeked',draw);v.addEventListener('loadedmetadata',draw);
draw();if(!v.paused)loop();})();
/* ---- the theorems, illustrated: one small hand-made case each; a plain animation that plays while it is on screen and then starts again ---- */
function theorem(id,cfg){var el=document.getElementById(id);if(!el)return;var q=function(r){return el.querySelector('[data-r="'+r+'"]');},svg=q('grid'),side=q('side'),stat=q('status'),C=50,timer=null,wait=null,S,X;
function build(){clear(svg);if(side)clear(side);S=cfg.init();X=cfg.build(svg,C,S);X.side=side;X.stat=stat;X.C=C;cfg.draw(S,X);}
function tick(){cfg.step(S);cfg.draw(S,X);if(cfg.done(S)){clearInterval(timer);timer=null;wait=setTimeout(function(){wait=null;build();go();},3200);}}
function go(){if(!timer&&!wait)timer=setInterval(tick,cfg.ms);}
function halt(){if(timer){clearInterval(timer);timer=null;}if(wait){clearTimeout(wait);wait=null;build();}}
el.style.setProperty('--gl',Math.round(cfg.ms*0.7)+'ms');build();
/* with reduced motion the final state is shown and nothing moves */
if(RM){var n=0;while(!cfg.done(S)&&n++<2000)cfg.step(S);cfg.draw(S,X);return;}
if('IntersectionObserver' in window)new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)go();else halt();});},{threshold:0.3}).observe(el.querySelector('.pf-panel'));else go();
document.addEventListener('visibilitychange',function(){if(document.hidden)halt();});}
/* one grid with its UAVs; affected locations are drawn in the anomaly colour, and every location can carry a small number */
function thgrid(host,G,C,anom,pos,ox){var g=ox==null?host:mk('g',{id:host.id+'-'+ox,transform:'translate('+ox+',0)'},host);if(ox==null)host.setAttribute('viewBox','-2 -2 '+(G*C+4)+' '+(G*C+4));
var L=gridSvg(g,G,C),r,c,num={};(anom||[]).forEach(function(p){mk('rect',{x:p[1]*C,y:p[0]*C,width:C,height:C,fill:ABN},L.cells);});var shade=mk('g',{},L.cells);
for(r=0;r<G;r++)for(c=0;c<G;c++)num[r+','+c]=mk('text',{x:c*C+C-4,y:r*C+C-5,'class':'th-n'},L.over);
return {L:L,shade:shade,num:num,uavs:pos.map(function(p){var u=icon(L,g,C);place(u,p,C);return u;})};}
function nbrs(p,G){var o=[],a;for(a=0;a<9;a++){var c=[p[0]+Math.floor(a/3)-1,p[1]+a%3-1];if(a!=4&&c[0]>=0&&c[0]<G&&c[1]>=0&&c[1]<G)o.push(c);}return o;}
function pick(a){return a[Math.floor(Math.random()*a.length)];}
function key(p){return p[0]+','+p[1];}
function best(o,w){var m=-1;o.forEach(function(c){m=Math.max(m,w[key(c)]);});return pick(o.filter(function(c){return w[key(c)]>=m-1e-9;}));}
function zeros(G){var w={},r,c;for(r=0;r<G;r++)for(c=0;c<G;c++)w[r+','+c]=0;return w;}
/* statistic or probability against time; marks = horizontal lines, lines = curves with an optional alarm star */
function thchart(ch,o){var x0=64,x1=540,y0=14,y1=236,X=function(t){return x0+t/o.xmax*(x1-x0);},Y=function(v){return y1-Math.min(v,o.ymax)/o.ymax*(y1-y0);},i;clear(ch);mk('rect',{x:0,y:0,width:560,height:300,fill:'#fff'},ch);
for(i=0;i<=o.xmax;i+=o.xs){mk('line',{x1:X(i),y1:y0,x2:X(i),y2:y1,stroke:'#e6e6e6'},ch);mk('text',{x:X(i),y:y1+24,'text-anchor':'middle','class':'tk'},ch).textContent=i;}
for(i=0;i<=o.ymax+1e-9;i+=o.ys){mk('line',{x1:x0,y1:Y(i),x2:x1,y2:Y(i),stroke:'#e6e6e6'},ch);mk('text',{x:x0-10,y:Y(i)+6,'text-anchor':'end','class':'tk'},ch).textContent=o.ys<1?i.toFixed(1):i;}
o.marks.forEach(function(m){var a={x1:x0,y1:Y(m.y),x2:x1,y2:Y(m.y),stroke:'#4d4d4d','stroke-width':1.6};if(m.dash)a['stroke-dasharray']='6 4';mk('line',a,ch);mk('text',{x:m.left?x0+8:x1-6,y:Y(m.y)+(m.below?20:-8),'text-anchor':m.left?'start':'end','class':'lg'},ch).textContent=m.label;});
o.lines.forEach(function(l){var d='',t;for(t=0;t<l.h.length;t++){if(l.h[t]==null)continue;d+=(d?(o.stairs?'H'+X(t).toFixed(1)+'V':'L'+X(t).toFixed(1)+' '):'M'+X(t).toFixed(1)+' ')+Y(l.h[t]).toFixed(1);}
if(d)mk('path',{d:d,fill:'none',stroke:LINE,'stroke-width':2.4,'stroke-linejoin':'round'},ch);
if(l.at){var st='',k,a,r;for(k=0;k<10;k++){a=-Math.PI/2+k*Math.PI/5;r=k%2?5:12;st+=(k?'L':'M')+(X(l.at)+r*Math.cos(a)).toFixed(1)+' '+(Y(o.star)+r*Math.sin(a)).toFixed(1);}mk('path',{d:st+'Z',fill:'#ffa500'},ch);if(l.label)mk('text',{x:Math.min(X(l.at),x1-40),y:Y(o.star)+30,'text-anchor':'middle','class':'lg'},ch).textContent=l.label;}});
mk('rect',{x:x0,y:y0,width:x1-x0,height:y1-y0,fill:'none',stroke:'#000','stroke-width':1.3},ch);mk('text',{x:(x0+x1)/2,y:292,'text-anchor':'middle','class':'al'},ch).textContent='Time step';
mk('text',{x:18,y:(y0+y1)/2,'text-anchor':'middle','class':'al',transform:'rotate(-90 18 '+(y0+y1)/2+')'},ch).textContent=o.ylab;}
/* the executed policy of the illustrations: stay with the probability given by the stay bias mixed with uniform exploration; otherwise move to the feasible neighbour with the largest evidence */
function stayp(S,G,eps){var p=S.pos[0],m=0;nbrs(p,G).forEach(function(c){m=Math.max(m,S.w[key(c)]);});S.gap=S.w[key(p)]-m;return (1-eps)/(1+Math.exp(-S.gap))+eps/9;}
function evid(S,inc){var p=S.pos[0],k;S.at=!!S.aff[key(p)];for(k in S.w){if(k==key(p))S.w[k]=S.at?S.w[k]+inc:0;else S.w[k]+=0.1;}}
/* Theorem 1, persistent coverage: before any change, every location keeps a positive hit rate */
theorem('ta',{ms:85,
init:function(){return {pos:[[0,0],[3,3]],w:zeros(4),v:zeros(4),t:0};},
build:function(svg,C,S){return thgrid(svg,4,C,[],S.pos);},
step:function(S){S.t++;S.pos.forEach(function(p,i){var o=nbrs(p,4).filter(function(c){return !S.pos.some(function(x,j){return j!=i&&x[0]==c[0]&&x[1]==c[1];});});o.push(p);S.pos[i]=Math.random()<0.2?pick(o):best(o,S.w);});
for(var k in S.w)S.w[k]+=0.1;S.pos.forEach(function(p){S.w[key(p)]=0;S.v[key(p)]++;});},
done:function(S){return S.t>=160;},
draw:function(S,X){var k,lo=1e9,n=0;S.pos.forEach(function(p,i){place(X.uavs[i],p,X.C);});clear(X.shade);
for(k in S.v){var f=S.t?S.v[k]/S.t:0,c=k.split(',');if(S.v[k]){n++;mk('rect',{x:c[1]*X.C,y:c[0]*X.C,width:X.C,height:X.C,fill:BLUE,opacity:Math.min(0.8,0.15+f*2.6).toFixed(2)},X.shade);}lo=Math.min(lo,f);X.num[k].textContent=S.t?Math.round(f*100)+'%':'';}
X.stat.textContent=!S.t?'Before any change, 2 UAVs monitor 16 locations.':(n<16?'Time step '+S.t+': '+n+' of 16 locations have been visited.':'Time step '+S.t+': every location has been visited, and the smallest hit rate is '+Math.round(lo*100)+'%.');}});
/* Theorem 2, evidence-based focusing: at an isolated affected location the stay probability approaches 1 - 8 eps / 9 */
theorem('tb',{ms:400,
init:function(){return {pos:[[0,0]],w:zeros(3),aff:{'1,1':1},t:0,h:[null],p:0,gap:0,at:false};},
build:function(svg,C,S){return thgrid(svg,3,C,[[1,1]],S.pos);},
step:function(S){var p=S.pos[0];if(Math.random()>=stayp(S,3,0.1))S.pos[0]=best(nbrs(p,3),S.w);S.t++;evid(S,2);S.p=stayp(S,3,0.1);S.h.push(S.at?S.p:null);},
done:function(S){return S.t>=32;},
draw:function(S,X){place(X.uavs[0],S.pos[0],X.C);for(var k in S.w)X.num[k].textContent=S.w[k].toFixed(1);
thchart(X.side,{xmax:32,xs:8,ymax:1,ys:0.2,ylab:'Stay Probability',star:0,marks:[{y:1-0.8/9,label:'Limit of the Theorem',dash:true,below:true}],lines:[{h:S.h}]});
X.stat.textContent=!S.t?'After the change, 1 UAV monitors 9 locations. The numbers are the evidence at each location.':(S.at?'The UAV observes the affected location. The local evidence gap is '+S.gap.toFixed(1)+', and the stay move has probability '+S.p.toFixed(2)+'.':'The UAV observes a normal location, where the evidence returns to 0.');}});
/* Theorem 3, detection-delay bound: the delay is inversely proportional to the hit rate of the affected location */
theorem('tc',{ms:280,routes:[[[1,1]],[[1,1],[1,2]],[[1,1],[1,2],[2,2],[2,1]]],
init:function(){return {t:0,s:[0,0,0],h:[[0],[0],[0]],al:[0,0,0]};},
build:function(svg,C,S){svg.setAttribute('viewBox','-2 -2 534 180');var me=this,gs=[0,190,380].map(function(ox,i){var g=thgrid(svg,3,C,[[1,1]],[me.routes[i][0]],ox);mk('text',{x:ox+75,y:172,'class':'th-c'},svg).textContent='Hit rate '+['1','1/2','1/4'][i];return g;});return {gs:gs};},
step:function(S){S.t++;for(var i=0;i<3;i++){var r=this.routes[i],p=r[S.t%r.length];if(!S.al[i]){if(p[0]==1&&p[1]==1)S.s[i]++;S.h[i].push(S.s[i]);if(S.s[i]>=8)S.al[i]=S.t;}}},
done:function(S){return S.al[2]>0;},
draw:function(S,X){var me=this;X.gs.forEach(function(g,i){var r=me.routes[i];place(g.uavs[0],S.al[i]?r[0]:r[S.t%r.length],X.C);});
thchart(X.side,{xmax:32,xs:8,ymax:10,ys:2,ylab:'Statistic',star:8,stairs:true,marks:[{y:8,label:'Detection Threshold',left:true}],lines:S.h.map(function(h,i){return {h:h,at:S.al[i],label:S.al[i]?'delay '+S.al[i]:''};})});
X.stat.textContent=!S.t?'Three UAVs observe an affected location at hit rates 1, 1/2 and 1/4.':(S.al[2]?'Halving the hit rate doubles the detection delay: 8, 16 and 32 time steps.':'The statistic increases by 1 at each observation of the affected location.');}});
/* corollary, clustered anomalies: a visited affected location dominates every unaffected location, and the alarm is triggered */
theorem('td',{ms:400,
init:function(){return {pos:[[0,0]],w:zeros(4),aff:{'1,1':1,'1,2':1,'2,1':1,'2,2':1},t:0,h:[0],al:0,gap:0,at:false};},
build:function(svg,C,S){return thgrid(svg,4,C,[[1,1],[1,2],[2,1],[2,2]],S.pos);},
step:function(S){var p=S.pos[0],k,m=0;if(Math.random()>=stayp(S,4,0.1))S.pos[0]=best(nbrs(p,4),S.w);S.t++;evid(S,1);for(k in S.w)m=Math.max(m,S.w[k]);S.h.push(m);if(!S.al&&m>=8)S.al=S.t;},
done:function(S){return S.al>0||S.t>=48;},
draw:function(S,X){place(X.uavs[0],S.pos[0],X.C);var k,a=0,u=0;for(k in S.w){X.num[k].textContent=S.w[k].toFixed(1);if(S.aff[k])a=Math.max(a,S.w[k]);else u=Math.max(u,S.w[k]);}
thchart(X.side,{xmax:48,xs:12,ymax:10,ys:2,ylab:'Statistic',star:8,stairs:true,marks:[{y:8,label:'Detection Threshold',left:true}],lines:[{h:S.h,at:S.al}]});
X.stat.textContent=!S.t?'After the change, 1 UAV monitors 16 locations with 4 clustered affected locations.':(S.al?'Alarm triggered at time step '+S.al+'. The evidence at the affected locations dominates every normal location.':'Largest evidence at an affected location: '+a.toFixed(1)+'. At a normal location: '+u.toFixed(1)+'.');}});
})();
</script>"""
ORDER=[k for t in THEMES for k in t["keys"]]
PSHORT=dict(SHORT,iise="Quality-driven coordination in multi-stage manufacturing")
def _pnav(k):
    i=ORDER.index(k); pv=ORDER[i-1] if i>0 else None; nx=ORDER[i+1] if i<len(ORDER)-1 else None
    return '<nav class="pn">%s%s</nav>'%(('<a class="pv" href="paper-%s.html"><span>Previous paper</span>&larr; %s</a>'%(pv,PSHORT[pv])) if pv else '<span></span>',
                                       ('<a class="nx" href="paper-%s.html"><span>Next paper</span>%s &rarr;</a>'%(nx,PSHORT[nx])) if nx else '<span></span>')
def paper_dispatchppo():
    t=[x for x in THEMES if "dispatchppo" in x["keys"]][0]; p=BYK0["dispatchppo"]
    bib="""@inproceedings{xia2026learning,
  title     = {Learning Collision-Free Dispatch Policies for Route-Wise Decision-Dependent Anomaly Detection},
  author    = {Xia, Xin and Zhang, Chen and Liu, Kaibo},
  booktitle = {Advances in Neural Information Processing Systems},
  publisher = {Curran Associates, Inc.},
  year      = {2026}
}"""
    b='<section class="pp-head"><p class="back"><a href="projects.html">Projects</a> <span>/</span> <a href="project-%s.html">%s</a></p>'%(t["slug"],t["title"])
    b+='<h1 class="pp-t">%s</h1>'%p["title"]
    b+='<p class="pp-au"><span><b>Xin Xia</b><sup>1</sup></span><span>Chen Zhang<sup>2</sup></span><span>Kaibo Liu<sup>1</sup></span></p>'
    b+='<p class="pp-aff"><span><sup>1</sup> Industrial and Systems Engineering, University of Wisconsin-Madison</span><span><sup>2</sup> Industrial Engineering, Tsinghua University</span></p>'
    b+='<p class="pp-ven">%s</p><div class="btns pp-btns">%s</div>'%(p["venue"],buttons(p,project=False))
    b+='<nav class="pp-jump" aria-label="On this page"><a href="#problem">Problem</a><a href="#replay">Replay</a><a href="#method">Method</a><a href="#guarantees">Guarantees</a><a href="#results">Results</a><a href="#deployment">Deployment</a><a href="#bibtex">BibTeX</a></nav></section>'
    b+='<section class="pp-sec"><div class="pp-two">'+_pvid("images/video/robotarium_demo.mp4","images/video/robotarium_demo_poster.jpg","images/fulls/dispatchppo_robotarium.jpg","Robotarium experiment: ten robots dispatched on the arena, with their trajectories and the detection statistic",1280,524,'Robot experiment (<a href="https://www.robotarium.gatech.edu" target="_blank" rel="noopener">Robotarium</a>)')+_pvid("images/video/dispatch_demo.mp4","images/video/dispatch_demo_poster.jpg","images/fulls/dispatchppo_ue.jpg","Five UAVs patrolling a forest in the Unreal Engine simulator; blue frustums are the camera footprints",1280,720,'Wildfire simulation (<a href="https://www.unrealengine.com" target="_blank" rel="noopener">Unreal Engine</a>)')+'</div>'
    b+='<p class="pp-lead">%s</p></section>'%p["abs"]
    b+='<section class="pp-sec" id="problem"><h2>A small fleet has to monitor a large region</h2><div class="pp-tx"><p>Each UAV observes only the location it visits, and anomalies may occur at unknown locations and times. Dispatch determines which locations are observed, and the observations update the evidence used for the next dispatch.</p><p>The goal is quickest detection under false-alarm control: keep the mean detection delay after a change (ARL<sub>1</sub>) small while the mean time to a false alarm (ARL<sub>0</sub>) stays above a required level. Moves are local, must stay inside the region, and must not collide.</p></div>'+_pfig("images/fulls/dp_overview.svg","Route-wise quickest detection with a coordinated UAV fleet: applications, and the constrained dispatch of a team at one time step",1971,697)+'</section>'
    b+=REPLAY_HTML.replace('@@EP@@',_demo_default()).replace('@@META@@',open(os.path.join(ROOT,'data','demo','dispatch_meta.json')).read()).replace('@@IDX@@',_demo_index())
    b+='<section class="pp-sec" id="method"><h2>DispatchNet samples a collision-free joint move without enumeration</h2><div class="pp-tx"><p>The dispatcher selects a joint move for all UAVs subject to local mobility and collision-avoidance constraints. Parallel per-UAV sampling may produce infeasible moves, while enumerating all joint moves scales exponentially, as 9<sup>N</sup> for N UAVs. DispatchNet addresses this with an encoder-decoder architecture, autoregressive decoding and dynamic feasibility masking.</p></div>'+DECODE_HTML+'<details class="pp-more"><summary>How the encoder, the decoder and the mask work</summary><div class="pp-tx"><p><strong>Encoder.</strong> Given the grid observation, a CNN block produces a spatial feature map. Each UAV forms a token from the feature at its current position, with identity and position embeddings. A Transformer encoder block then models inter-UAV interactions, such as congestion and mutual exclusion.</p><p><strong>Autoregressive decoder.</strong> The decoder assigns moves sequentially, from UAV 1 to UAV N. For each UAV it scores the 9 local moves, using the embedding of this UAV and the move assigned to the previous UAV.</p><p><strong>Dynamic feasibility mask.</strong> To prevent collisions during decoding, the mask reserves the destinations already assigned to earlier UAVs and the current positions of UAVs not yet decoded. This prevents both direct collisions and position swaps, and every UAV always retains at least the stay move. Each move is sampled from the masked distribution, so the joint move is collision-free and is generated in O(K+N) time for K locations and N UAVs.</p></div></details>'+DECIDE_HTML+'</section>'
    b+='<section class="pp-sec" id="guarantees"><h2>Coverage, focusing and detection delay are guaranteed</h2><div class="pp-tx"><p>Learning has two stages. Stage I trains the policy offline in simulated environments with PPO and proxy rewards. Stage II executes it online, mixed with uniform exploration.</p></div>'+THM_HTML+'</section>'
    b+='<section class="pp-sec" id="results"><h2>Detection delay under false-alarm control</h2><table class="pp-spec"><tr><th>Environment</th><td>5&times;5 to 30&times;30 grids, 1 to 30 UAVs, 2 to 10 anomalies</td></tr><tr><th>Anomaly</th><td>mean shift &Delta; &isin; {1, 2, 3, 4}, starting at a time drawn uniformly from 5 to 50</td></tr><tr><th>Metric</th><td>ARL<sub>1</sub> at ARL<sub>0</sub> = 370, 1,000 replications per setting</td></tr></table>'+_pfig("images/fulls/dp_delay.svg","Detection delays (ARL1) under calibrated false-alarm control across grid sizes and fleet sizes, for Random, Greedy, Patrolling, Look-ahead and DispatchPPO",2200,1088)+'<div class="pp-tx"><p>DispatchPPO decides within a few milliseconds per time step, whereas Look-ahead needs seconds to about a minute as the fleet or the grid grows.</p></div><details class="pp-more"><summary>Per-step decision time against fleet size and grid size</summary>'+_pfig("images/fulls/dp_time.svg","Wall-clock time per decision (log scale) for Greedy, Look-ahead and DispatchPPO, against fleet size on a 10 by 10 grid (left) and against grid size with 5 UAVs (right)",2200,765)+'</details></section>'
    b+='<section class="pp-sec" id="deployment"><h2>Deployment on robots and on a real wildfire</h2><h3>Robotarium: 10 robots, 5 anomalies from t = 250 s</h3>'+'<div class="rb" id="rb"><figure class="pp-fig"><div class="rb-card"><a class="media rb-cam" href="images/video/robotarium_camera_poster.jpg" data-lb="Robotarium deployment of DispatchPPO with 10 robots: camera view of the arena, robot trajectories over time (crosses mark the affected locations), and the detection statistic over time" data-video="images/video/robotarium_demo_hd.mp4"><video src="images/video/robotarium_camera.mp4" poster="images/video/robotarium_camera_poster.jpg" muted loop playsinline autoplay preload="auto" style="aspect-ratio:1740/980"></video></a><div class="rb-side"><div class="rb-p"><span class="rb-h">Trajectories over time</span><svg data-r="traj" viewBox="0 0 320 150" role="img" aria-label="Trajectories of the ten robots on the arena, with the affected locations marked"></svg></div><div class="rb-p"><span class="rb-h">Detection statistic</span><svg data-r="stat" viewBox="0 0 320 150" role="img" aria-label="Detection statistic over time with the change point and the detection threshold"></svg></div></div></div><div class="rb-ctl"><div class="rb-bar" data-r="bar" role="slider" tabindex="0" aria-label="Time in the run" aria-valuemin="0" aria-valuemax="400" aria-valuenow="0"><i data-r="fill"></i><b style="left:62.5%"></b><b style="left:71.25%"></b></div><div class="rb-row"><span class="rb-l">Jump to</span><button type="button" class="pc-rs" data-t="0">Start</button><button type="button" class="pc-rs" data-t="250">Change point</button><button type="button" class="pc-rs" data-t="285">Alarm triggered</button><span class="rb-t" data-r="time" aria-live="off">t = 0 s</span></div></div><figcaption>Robotarium deployment of DispatchPPO with 10 robots: camera view of the arena, robot trajectories over time (crosses mark the affected locations), and the detection statistic over time</figcaption></figure><script type="application/json" id="rb-data">'+open(os.path.join(ROOT,'data','demo','robotarium_run.json')).read()+'</script></div>'+'<h3>Cherrywood wildfire (2021): 2 UAVs on a 10&times;10 grid reconstructed from satellite frames</h3>'+_pfig("images/fulls/dp_wildfire.svg","Dispatch by DispatchPPO and by the Look-ahead baseline on the reconstructed wildfire; red intensity indicates the fire",2051,581)+'</section>'
    b+='<section class="pp-sec" id="bibtex"><div class="pp-bh"><h2>BibTeX</h2><button class="pp-copy" id="bibcopy" type="button">Copy</button></div><pre class="pp-bib" id="bib">%s</pre></section>'%bib
    b+=_pnav("dispatchppo")
    b+=PAPER_JS
    b+="""<script>(function(){var b=document.getElementById('bibcopy'),t=document.getElementById('bib');if(!b)return;b.addEventListener('click',function(){var done=function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy';},1600);};var sel=function(){var r=document.createRange();r.selectNodeContents(t);var s=window.getSelection();s.removeAllRanges();s.addRange(r);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t.textContent).then(done,sel);}else{sel();}});})();</script>"""
    # hyphenated words in the title never break at the hyphen
    b=re.sub(r'(<h(1)[^>]*>)(.*?)(</h\2>)',lambda m:m.group(1)+re.sub(r'(?<![\w<&/-])([A-Za-z]+(?:-[A-Za-z]+)+)',r'<span class="nb">\1</span>',m.group(3))+m.group(4),b,flags=re.S)
    open(os.path.join(ROOT,"paper-dispatchppo.html"),"w").write(shell("%s - Xin Xia"%p["title"],b,"projects"))
paper_dispatchppo()
BIBCOPY_JS="""<script>(function(){var b=document.getElementById('bibcopy'),t=document.getElementById('bib');if(!b)return;b.addEventListener('click',function(){var done=function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy';},1600);};var sel=function(){var r=document.createRange();r.selectNodeContents(t);var s=window.getSelection();s.removeAllRanges();s.addRange(r);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t.textContent).then(done,sel);}else{sel();}});})();</script>"""
BIBS={
 "hass":"""@article{xia2026hierarchical,
  title   = {Multi-Agent Reinforcement Learning for Anomaly Detection with Hierarchical Adaptive Sampling Strategy},
  author  = {Xia, Xin and Guo, Jie and Zheng, Ziqian and Ma, Yujie and Zhang, Chen and Liu, Kaibo},
  journal = {Technometrics},
  year    = {2026},
  note    = {Accepted}
}""",
 "bsac":"""@article{ma2025bilevel,
  title   = {A Deep Reinforcement Learning Method Solving Bilevel Optimization for Product Design Considering Remanufacturing},
  author  = {Ma, Yujie and Xia, Xin and Guo, Jie and Zhang, Chen},
  journal = {IEEE Transactions on Engineering Management},
  volume  = {72},
  pages   = {573--590},
  year    = {2025},
  doi     = {10.1109/TEM.2025.3535771}
}""",
 "ijpe":"""@article{ma2025designchange,
  title   = {Bilevel Joint Optimization for Product Design Changes with a Resilient Supply Chain Based on Deep Reinforcement Learning},
  author  = {Ma, Yujie and Xia, Xin and Liu, Peiyao and Zhang, Chen},
  journal = {International Journal of Production Economics},
  volume  = {290},
  pages   = {109791},
  year    = {2025},
  doi     = {10.1016/j.ijpe.2025.109791}
}""",
 "causal":"""@article{le2024multiagent,
  title   = {Multi-Agent Causal Discovery Using Large Language Models},
  author  = {Le, Hao Duong and Xia, Xin and Xu, Haijie and Zhang, Chen},
  journal = {arXiv preprint arXiv:2407.15073},
  year    = {2024}
}""",
}
def paper_generic(k):
    t=[x for x in THEMES if k in x["keys"]][0]; p=BYK0[k]
    b='<section class="pp-head"><p class="back"><a href="projects.html">Projects</a> <span>/</span> <a href="project-%s.html">%s</a></p>'%(t["slug"],t["title"])
    b+='<h1 class="pp-t">%s</h1>'%p["title"]
    b+='<p class="pp-au">%s</p>'%"".join('<span>%s</span>'%a.strip() for a in re.split(r',\s*and\s+|\s+and\s+|,\s*',p["au"]) if a.strip())
    b+='<p class="pp-ven">%s%s</p>'%(p["venue"],' <span class="st">(%s)</span>'%p["status"] if p["status"] else "")
    if p["award"]: b+='<div class="pp-aw">%s</div>'%award_html(p)
    bt=buttons(p,project=False)
    if bt: b+='<div class="btns pp-btns">%s</div>'%bt
    b+='</section><section class="pp-sec"><p class="pp-lead">%s</p>'%p["abs"]
    if k in DEMOS: b+=gallery(DEMOS[k])
    b+='</section>'
    if k in BIBS: b+='<section class="pp-sec" id="bibtex"><div class="pp-bh"><h2>BibTeX</h2><button class="pp-copy" id="bibcopy" type="button">Copy</button></div><pre class="pp-bib" id="bib">%s</pre></section>'%BIBS[k]
    b+=_pnav(k)+(BIBCOPY_JS if k in BIBS else "")
    b=re.sub(r'(<h(1)[^>]*>)(.*?)(</h\2>)',lambda m:m.group(1)+re.sub(r'(?<![\w<&/-])([A-Za-z]+(?:-[A-Za-z]+)+)',r'<span class="nb">\1</span>',m.group(3))+m.group(4),b,flags=re.S)
    open(os.path.join(ROOT,"paper-%s.html"%k),"w").write(shell("%s - Xin Xia"%p["title"],b,"projects"))
for _k in ORDER:
    if _k!="dispatchppo": paper_generic(_k)

# ---------------------------------------------------------------- publications page (text only)
GROUPS=[("Journal articles","J",["hass","bsac","ijpe"]),
        ("Conference papers","C",["dispatchppo","scan"]),
        ("Under review and preprints","U",["kappa","msom","iise","causal"])]
BYK={p["k"]:p for p in PUBS}
def entry(tag,p):
    status=' <span class="st">(%s)</span>'%p["status"] if p["status"] else ""
    links=std_links(p)
    ti=p["title"]
    if p["k"] in PAGE_OF: ti='<a href="%s#proj-%s">%s</a>'%(PAGE_OF[p["k"]],p["k"],ti)
    ln=" ".join('<a href="%s"%s>%s</a>'%(u,"" if u.startswith("project-") else ' target="_blank" rel="noopener"',l) for l,u in links)
    aw=""
    if p["award"]:
        txt=p["award"].replace('<b class="win">Winner</b>',"Winner, ")
        aw=' <span class="awi">%s</span>'%(('<a href="%s" target="_blank" rel="noopener">%s</a>'%(p["award_url"],txt)) if p.get("award_url") else txt)
    return '<li id="%s"><span class="tag">[%s]</span><div>%s. <span class="pt">%s.</span> <em>%s</em>%s.%s<div class="pl">%s</div></div></li>'%(p["k"],tag,p["au"].replace(", and "," and ") if p["au"].count(",")<2 else p["au"],ti,p["venue"],status,aw,ln)
pubs='<section id="publications"><h1>Publications</h1>'
for title,letter,keys in GROUPS:
    n=len(keys)
    pubs+='<h2>%s</h2><ol class="plist">%s</ol>'%(title,"".join(entry("%s%d"%(letter,n-i),BYK[k]) for i,k in enumerate(keys)))
pubs+='<h2>Patents</h2><ol class="plist">'+"".join('<li><span class="tag">[P%d]</span><div>%s <span class="pt">%s</span> Chinese invention patent, <span class="mono">%s</span>.</div></li>'%(len(PATENTS)-i,a,t,n) for i,(n,a,t) in enumerate(PATENTS))+'</ol></section>'
open(os.path.join(ROOT,"publications.html"),"w").write(shell("Publications - Xin Xia",pubs,"publications"))

# ---------------------------------------------------------------- talks page
TALKS=[("dispatchppo",None,"INFORMS Annual Meeting, San Francisco, CA, Nov 2026","","data/certificates/INFORMS2026_presentation_certificate.pdf"),
       ("scan",None,"INFORMS QSR Best Refereed Paper Competition, INFORMS Annual Meeting, San Francisco, CA, Nov 2026",'<a href="%s" target="_blank" rel="noopener">Winner</a>'%AW1,""),
       (None,"Interactive Resource Allocation and Anomaly Detection via Multi-Agent Reinforcement Learning","INFORMS Annual Meeting, Atlanta, GA, Oct 2025","","data/certificates/INFORMS2025_presentation_certificate.pdf"),
       (None,"Interactive Resource Planning and Change Detection via Multi-agent Reinforcement Learning","IISE QCRE Best Track Paper Competition, IISE Annual Conference &amp; Expo, Atlanta, GA, Jun 2025",'<a href="%s" target="_blank" rel="noopener">Finalist</a>'%AW2,"")]
talks='<section id="talks"><h1>Invited talks</h1><ol class="plist">'+"".join(
    '<li><span class="tag">[T%d]</span><div><span class="pt">%s.</span> <em>%s</em>.%s%s</div></li>'%(len(TALKS)-i,BYK[k]["title"] if k else t,ev,(' <span class="awi">%s</span>'%aw) if aw else "",('<div class="pl"><a href="%s" target="_blank" rel="noopener">Certificate</a></div>'%c) if c else "")
    for i,(k,t,ev,aw,c) in enumerate(TALKS))+'</ol></section>'
open(os.path.join(ROOT,"talks.html"),"w").write(shell("Invited talks - Xin Xia",talks,"talks"))

# old multi-page URLs redirect to the matching section
for fn,sec in [("news.html","news"),("cv.html","experience")]:
    open(os.path.join(ROOT,fn),"w").write(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Xin Xia</title><meta http-equiv="refresh" content="0; url=index.html#{sec}"><link rel="canonical" href="https://xxia99.com/#{sec}"></head><body><a href="index.html#{sec}">Continue to xxia99.com</a></body></html>\n')
print("built index.html, publications.html and projects.html with",len(PUBS),"publications")

# ---------------------------------------------------------------- design checks (see project design rules)
def check_design():
    """Fail the build on: figures with transparency or SVG masks/filters; long dashes in generated pages."""
    import glob
    from PIL import Image
    bad=[]
    for f in sorted(glob.glob(os.path.join(ROOT,"images","fulls","*"))+glob.glob(os.path.join(ROOT,"images","mini","*"))):
        low=f.lower()
        if low.endswith(".svg"):
            t=open(f,errors="ignore").read()
            if "<mask" in t or "<filter" in t: bad.append("SVG uses mask/filter: "+os.path.relpath(f,ROOT))
        elif low.endswith(".png"):
            im=Image.open(f)
            if im.mode in ("RGBA","LA") and im.getchannel("A").getextrema()[0]<255: bad.append("PNG has transparency: "+os.path.relpath(f,ROOT))
    for f in sorted(glob.glob(os.path.join(ROOT,"*.html"))):
        t=open(f,encoding="utf-8",errors="ignore").read()
        for ch,name in (("\u2013","en dash"),("\u2014","em dash"),("&ndash;","en dash"),("&mdash;","em dash")):
            if ch in t: bad.append("%s in %s"%(name,os.path.basename(f)))
    if bad:
        print("DESIGN CHECK FAILED:"); [print("  - "+b) for b in bad]; raise SystemExit(1)
    print("design checks passed")
check_design()

# ---------------------------------------------------------------- link papers that have their own page
PAPER_PAGES={p["k"]:p["title"] for p in PUBS}
for _f in sorted(os.listdir(ROOT)):
    if not _f.endswith(".html"): continue
    _p=os.path.join(ROOT,_f); _h=open(_p).read(); _o=_h
    for _k,_t in PAPER_PAGES.items():
        _h=re.sub(r'project-[a-z-]+\.html#proj-%s\b'%_k,'paper-%s.html'%_k,_h)
        if _f.startswith("project-"):
            _h=_h.replace('<h3 class="t">%s</h3>'%_t,'<h3 class="t"><a href="paper-%s.html">%s</a></h3>'%(_k,_t))
    if _h!=_o: open(_p,"w").write(_h)
