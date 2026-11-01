p = '/workspace/index.html'
s = open(p, encoding='utf-8').read()
def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, "anchor count %d != %d: %r" % (s.count(old), cnt, old[:90])
    s = s.replace(old, new)

# ---- A. Audio engine: replace global BGM with per-slide music tracks ----
old_bgm = """  var bgm = {
    nodes: [], master: null, on: false,
    start: function(){
      if (this.on) return;
      var ctx = ensureAudio(); if (!ctx) return;
      this.master = ctx.createGain(); this.master.gain.value = 0;
      this.master.connect(ctx.destination);
      var ch1 = ctx.createGain(), ch2 = ctx.createGain(), pad = ctx.createOscillator();
      ch1.gain.value = .5; ch2.gain.value = .5;
      pad.type = 'triangle'; pad.frequency.value = 65.4;
      var pf = ctx.createBiquadFilter(); pf.type = 'lowpass'; pf.frequency.value = 320;
      pad.connect(pf); pf.connect(this.master);
      pad.start();
      this.nodes = [pad];
      this.seqTimer = setInterval(function(){ AUDIO.bgm.tick(); }, 2000);
      this.master.gain.linearRampToValueAtTime(.028, ctx.currentTime + 1.5);
      this.on = true;
    },
    tick: function(){
      if (!this.on || !this.master) return;
      var ctx = audioCtx, scale = [130.8, 155.6, 196.0, 233.1, 261.6], t = ctx.currentTime + .05;
      for (var i = 0; i < 2; i++){
        var f = scale[(Math.random() * scale.length) | 0] * (i ? 2 : 1);
        var o = ctx.createOscillator(), g = ctx.createGain();
        o.type = 'sine'; o.frequency.value = f;
        g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.5, t + .4); g.gain.exponentialRampToValueAtTime(.001, t + 1.9);
        o.connect(g); g.connect(i ? ch2Ref() : ch1Ref()); o.start(t); o.stop(t + 2);
      }
      function ch1Ref(){ return AUDIO.bgm.ch1 || AUDIO.bgm.master; }
      function ch2Ref(){ return AUDIO.bgm.ch2 || AUDIO.bgm.master; }
    },
    stop: function(){
      if (!this.on) return;
      var ctx = audioCtx; clearInterval(this.seqTimer);
      try { this.master.gain.linearRampToValueAtTime(0, ctx.currentTime + .4); } catch(e){}
      var ns = this.nodes.slice(); setTimeout(function(){ ns.forEach(function(o){ try{o.stop();}catch(e){} }); }, 700);
      this.nodes = []; this.on = false;
    }
  };"""
if s.count(old_bgm) != 1:
    # locate block boundaries robustly
    i0 = s.index('  var bgm = {')
    i1 = s.index('};', s.index('stop: function(){', i0)) + 2
    old_bgm = s[i0:i1]
new_bgm = """  /* Revision 2: per-slide background music (one track at a time). */
  var MUSIC_DEFS = {
    1:{root:130.8, iv:[0,7,12,7],  wave:'sine',     vol:.030, spb:1.15},
    2:{root:146.8, iv:[0,5,9,5],   wave:'triangle', vol:.026, spb:1.30},
    3:{root:110.0, iv:[0,7,10,7],  wave:'sine',     vol:.022, spb:1.50},
    4:{root:164.8, iv:[0,4,7,11],  wave:'triangle', vol:.020, spb:0.95},
    5:{root:123.5, iv:[0,3,7,10],  wave:'sine',     vol:.028, spb:1.35},
    6:{root:98.0,  iv:[0,7,12,15], wave:'triangle',vol:.026, spb:1.20},
    7:{root:174.6, iv:[0,5,9,12],  wave:'sine',     vol:.024, spb:1.10},
    8:{root:116.5, iv:[0,7,12,7],  wave:'triangle', vol:.028, spb:1.25},
    9:{root:139.7, iv:[0,4,9,4],   wave:'sine',     vol:.026, spb:1.15},
    10:{root:130.8,iv:[0,7,12,16], wave:'sine',     vol:.032, spb:1.05}
  };
  var bgm = {
    on:false, idx:0, def:null, master:null, timer:null, step:0, ducked:false,
    play: function(idx){
      this.stopNow(true);
      var ctx = ensureAudio(); if(!ctx) return false;
      this.def = MUSIC_DEFS[idx] || MUSIC_DEFS[1]; this.idx = idx;
      this.master = ctx.createGain(); this.master.gain.value = this.ducked ? this.def.vol*0.3 : this.def.vol;
      this.master.connect(ctx.destination);
      this.step = 0;
      var self = this;
      this.voices();
      this.timer = setInterval(function(){ self.tick(); }, Math.round(self.def.spb*1000));
      this.on = true; return true;
    },
    voices: function(){
      var ctx = audioCtx, d = this.def, t = ctx.currentTime + .05;
      var n = d.iv.length, i = this.step % n, semi = d.iv[i];
      var f = d.root * Math.pow(2, semi/12);
      var o = ctx.createOscillator(), g = ctx.createGain();
      o.type = d.wave; o.frequency.value = f;
      var lp = ctx.createBiquadFilter(); lp.type='lowpass'; lp.frequency.value = 900;
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.5, t+.12); g.gain.exponentialRampToValueAtTime(.001, t + d.spb*1.9);
      o.connect(lp); lp.connect(g); g.connect(this.master); o.start(t); o.stop(t + d.spb*2 + .1);
      if (i === 0){
        var b = ctx.createOscillator(), bg2 = ctx.createGain();
        b.type='sine'; b.frequency.value = d.root/2;
        bg2.gain.setValueAtTime(0,t); bg2.gain.linearRampToValueAtTime(.45,t+.15); bg2.gain.exponentialRampToValueAtTime(.001,t+d.spb*3.4);
        b.connect(bg2); bg2.connect(this.master); b.start(t); b.stop(t+d.spb*3.6);
      }
      this.step++;
    },
    tick: function(){ if (this.on) this.voices(); },
    duck: function(on){
      this.ducked = !!on;
      if (this.on && this.master && audioCtx){
        var v = this.def.vol * (on ? 0.3 : 1);
        try{ this.master.gain.cancelScheduledValues(audioCtx.currentTime); this.master.gain.linearRampToValueAtTime(v, audioCtx.currentTime+.25);}catch(e){}
      }
    },
    stopNow: function(silent){
      if (this.timer){ clearInterval(this.timer); this.timer = null; }
      if (this.on && this.master && audioCtx){
        var m = this.master, ns = null;
        try{ m.gain.linearRampToValueAtTime(0, audioCtx.currentTime + (silent ? .18 : .35)); }catch(e){}
      }
      this.on = false; this.idx = 0; this.master = null;
    }
  };"""
rep(old_bgm, new_bgm)

# ---- B. Remove the old bgmBtn wiring in bindGlobalUI ----
old_btn = """    $('bgmBtn').addEventListener('click', function(){
      if (AUDIO.bgm.on){ AUDIO.bgm.stop(); setAudioButton('bgmBtn', false, 'Music'); }
      else { AUDIO.unlock(); AUDIO.bgm.start(); setAudioButton('bgmBtn', true, 'Music'); }
    });"""
if s.count(old_btn) != 1:
    i0 = s.index("    $('bgmBtn').addEventListener")
    depth = 0; j = s.index('{', i0)
    # find matching close by counting braces from first '{' of handler
    k = i0; openCount = 0; started = False
    while True:
        c = s[k]
        if c == '{': openCount += 1; started = True
        elif c == '}':
            openCount -= 1
            if started and openCount == 0: break
        k += 1
    old_btn = s[i0:k+1]
new_btn = """    /* Per-slide music toggle (Revision 2) */
    $('musicToggle').addEventListener('click', function(){
      if (AUDIO.bgm.on){ AUDIO.bgm.stopNow(); setMusicBtn(false); }
      else { AUDIO.unlock(); var ok = AUDIO.bgm.play(cur + 1); setMusicBtn(!!ok); }
    });"""
rep(old_btn, new_btn)

# ---- C. setAudioButton -> setMusicBtn helper ----
old_sab_i = s.index('function setAudioButton')
old_sab = s[old_sab_i:s.index('\n}\n', old_sab_i)+2]
new_sab = """function setMusicBtn(on){
  var b = $('musicToggle'); if (!b) return;
  b.setAttribute('aria-pressed', on ? 'true' : 'false');
  b.textContent = on ? 'Music \u00b7 On' : 'Music \u00b7 Off';
}
"""
rep(old_sab, new_sab)

open(p,'w',encoding='utf-8').write(s)
print("audio engine edits OK")
