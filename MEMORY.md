# MEMORY.md - Long Term Memory

## User (Thomas)
- **Timezone**: Eastern US (ET)
- **Sleep hours**: 21:00 - 05:00 (9PM - 5AM)
- **Active hours**: 06:00 - 21:00 ET
- **Background**: Navy Nuclear program, teaches at Newport. Plan 2027 transition to space/nuclear/tech.
- **Goals**: Rapid financial growth, long-term ambitious projects in 40s/50s
- **Values**: Free speech, individual rights, human flourishing, space exploration
- **Concerns**: Negative population growth, future of humanity with AI
- **Preference**: Useful tools over quick ad-revenue sites (but accepts strategically)
- **Physics/Eng**: Nuclear trained, ion beam research (UNT with Dr. Duncan Weathers)

## Memory System v2 (Feb 2026)
**Problem**: Token bloat from loading full conversation history in `memory_search()`
**Solution**: Tiered storage with manual indexing

### Hierarchy
1. **.index** - Manual lookup table (always load, ~200 tokens)
2. **Daily files** - Today/yesterday only (~500-1K tokens)
3. **Project folders** - memory/projects/<name>/README.md (~300 each)
4. **MEMORY.md** - This file: distilled preferences only (~500-1K tokens)

### Archival Policy
- Daily files >7 days: summarize into MEMORY.md or delete
- Never load >2 days unless explicitly requested
- Keep project folders for active work

## Active Projects
- **site-builder**: Skill for rapid site creation (templates: landing-page, portfolio, blog, dashboard)

## Preferences
- Frequent updates 06:00-16:00 ET (hourly during work hours)
- Proactive recommendations, not just problems
- When building sites: useful tools > ad revenue

## Patterns
- "Get it installed for me" = execute without excessive questions
- Short answers like "Okay" = acknowledge, continue
- "Fix it" = something's broken, check current work
