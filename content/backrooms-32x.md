Title: A Backrooms raycaster for the Sega 32X
Date: 2026-07-22
Slug: backrooms-32x
Category: Game Design
Tags: sega-32x, sh-2, raycasting, homebrew, retro

I've been building a first-person Backrooms raycasting engine for the
Sega 32X, and this week
[Tom's Hardware wrote it up](https://www.tomshardware.com/video-games/retro-gaming/1994-sega-32x-gets-first-person-backrooms-game-with-raycasting-engine-retro-hardware-tour-de-force-includes-yellow-rooms-buzzing-fluorescents-endless-procedurally-generated-levels).

The 32X is a mushroom-shaped add-on Sega bolted onto the Genesis in
1994 and abandoned by 1996. It has two Hitachi SH-2 processors at 23 MHz,
256 KB of RAM, a paletted 320×224 framebuffer, no GPU, and no floating
point. It is, in other words, exactly enough machine for a raycaster —
if you write one from scratch and use everything the box has.

This is an engine in active development, not a finished game. The current 
build/release has one objective beyond wandering the halls — which is to 
find the exit. For the Backrooms, arguably on-theme.

## The engine

The engine is C99 (`-ffreestanding`) with hand-rolled SH-2 assembly in
the hot loops. What it does:

- **Textured DDA raycasting** with distance fog and dynamic ceiling
  lighting — the fluorescent fixtures are real geometry in world space,
  so the tube quads rotate with the room when you turn instead of
  sitting pinned to the screen.
- **Slab partitions**: full-height dividers, half-height cubicle walls,
  and countertops you can see over. Liminal office space needs cubicles.
- **Adaptive load-balanced rendering across both SH-2s.** The two CPUs
  split the screen, and the split point moves frame to frame based on
  who finished late.
- **The 68000 holds the console together.** All HUD and menu text 
  renders on the Genesis VDP tile layer, drawn by the otherwise-idle 68K 
  and composited over the 3D essentially for free.
- **Procedurally generated levels**, so the hallways really do go on
  forever, plus crawl/crouch with full eye-height perspective and a 3D
  cardboard-box intro rendered live — not a video.

## Community-driven by design

You don't need a 32X — or even an emulator — to build for this engine.
A browser-based level editor lets anyone design a map and immediately
walk it in a first-person preview, right in the browser. No hardware 
necessary, no toolchain, no setup. If you want to clone and build 
locally you can, but the contribution path doesn't require it.

The editor uses a GitHub OAuth integration — when your map is ready you 
submit it as a pull request against the engine without leaving the browser.
When the PR merges, the pipeline automatically releases a new playable ROM 
to itch.io. Community map submissions go into the released game 
immediately. The distance from 'I drew a hallway' to 'strangers are walking 
my hallway on real 1994 hardware' is one merge.

The build itself lives in CI. Every pull request is linted and then
compiled against a pinned marsdev toolchain in GitHub's runners, so a
contributor's map is proven to link into a real ROM before it merges,
and an ad-hoc build of the current engine is one workflow dispatch
away. The map editor ships as a Docker image, so the whole contribution
stack runs anywhere Docker does. This eliminates a need for a cross-compiler 
on a dev machine — the pipeline is the build machine.

## What dead-platform work is actually like

Marsdev replaces a long dead vendor SDK, and with very little
official documentation - you work from community reverse-engineering
notes and behavior observed on real hardware. A few of the things the
32X dev has taught me:

- The stock open-source toolchain boots the secondary SH-2 into a state
  the documentation doesn't describe. Currently you read the startup 
  assembly and fix it yourself.
- The SH-2 data cache is write-through with no coherency between the
  two CPUs, so cross-CPU shared state goes through a cache-through
  mirror of the address space (`addr | 0x20000000`) — a trick that
  exists in scattered forum posts, not in any manual.
- At one point a doubled audio buffer built and linked cleanly, then
  silently landed on top of the CPU stack — the linker's memory map ran
  a few kilobytes past where the stack actually sits, and the machine
  has no memory protection to complain. Checking the symbol table
  against the real stack address is what caught it. A clean build is
  not proof it fits.

I've been publishing dev notes to the itch.io devlog.

## On building this with an LLM

I used Claude Code throughout, and I'm straightforward about that. 
The division of labor: I drove the architecture, picked the
optimization targets, and read the hardware — the 32X barely exists in
any model's training data, so platform behavior had to be discovered on
real hardware and fed back in. Claude did per-step research, wrote code
under direction, and reasoned through the dual-CPU and cache-coherency
models. The DEVLOG doubles as a record of that collaboration: what an
LLM is genuinely good at on a platform it has never seen, and where the
human has to hold the map.

## Try it

The engine is free and open source. Runs on real 32X hardware, MiSTer
FPGA, and any 32X-capable emulator (RetroArch, BlastEm, Ares, Kega
Fusion).

- Source: [github.com/mholzinger/32x-builder](https://github.com/mholzinger/32x-builder)
- Play it: [paisleyboxers.itch.io/backrooms32x](https://paisleyboxers.itch.io/backrooms32x)
- Coverage: [Tom's Hardware](https://www.tomshardware.com/video-games/retro-gaming/1994-sega-32x-gets-first-person-backrooms-game-with-raycasting-engine-retro-hardware-tour-de-force-includes-yellow-rooms-buzzing-fluorescents-endless-procedurally-generated-levels)

Welcome to the cutting edge of 1994.
