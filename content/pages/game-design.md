Title: Game Design
Date: 2026-05-20
Slug: game-design

Retro / homebrew console work, original games, and tools for the Intellivision community.

### [Backrooms 32X](https://paisleyboxers.itch.io/backrooms32x) — first-person raycaster for the Sega 32X
A Backrooms raycasting engine written from scratch in C and SH-2 assembly for the 1994 Sega 32X — dual-CPU load-balanced rendering, procedurally generated levels, and a browser-based level editor with a community-map pipeline (map PR + merge = released ROM). Covered by [Tom's Hardware](https://www.tomshardware.com/video-games/retro-gaming/1994-sega-32x-gets-first-person-backrooms-game-with-raycasting-engine-retro-hardware-tour-de-force-includes-yellow-rooms-buzzing-fluorescents-endless-procedurally-generated-levels). [Write-up](/backrooms-32x.html) · [Source on GitHub.](https://github.com/mholzinger/32x-builder)

### [Intellivision Overlay Editor](https://intellivision-overlay-editor.fly.dev/)
A full browser-based suite for designing custom Intellivision controller overlays and box art for the Sprint USB controllers. Live SVG preview, customizable button layouts, gradient text styling, 58 bundled overlay-optimized fonts, and multiple export formats (PNG, framed overlays, project files). [Source on GitHub.](https://github.com/mholzinger/intellivision-overlay-editor)

### [Space Intruders](https://paisleyboxers.itch.io/space-intruders) — original Intellivision homebrew
An original game written for the Intellivision. Available on itch.io.

### [neoDS (PicoDS build)](https://github.com/mholzinger/neoDS)
Fork of the 2008 NeoDS NeoGeo AES/MVS emulator for Nintendo DS, updated to 2026 MAME sets and compiled for PicoDS. M68000 + Z80 CPU emulation, streamed ROM data, textured-quad graphics, ADPCM/PSG audio.

### [intv2-convert](https://github.com/mholzinger/intv2-convert)
ROM format conversion utility for Intellivision FPGA platforms — converts Intellivision ROMs to the INTV2 chunked-loading format used by Analogue Nt Mini Noir and Analogue Pocket cores. Native C++ binary with optional GUI plus matching Python scripts; accepts jzIntv BIN/CFG pairs, IntyBASIC listings, and self-describing ROMs.
