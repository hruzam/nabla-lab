# _mail/ — the lab bus (NON-CANONICAL · gitignored)

Working-state message bus for nabla-lab. **Nothing here is canon**. Only this `README.md`
+ `.gitignore` are tracked; everything else is gitignored and drainable (extract what matters
into its real home, then delete).

## What goes where
- **Requests / proposals to a specific seat** → `_mail/<seat>/inbox/<sender>.<scope>.<YYYY-MM-DD>.md`
- **Broadcasts to everyone** → `_mail/toAll/inbox/`
- **Fast status / "what I just did"** → `session/pulse.md` (NOT here)

## Seat addresses (current lab)

```
_mail/atlas/        — primitive requests, harness changes
_mail/flight/       — project direction, structural decisions
_mail/oraculum/     — research leads, synthesis requests
_mail/monkey/       — operator notes-to-self
_mail/toAll/        — broadcasts (model changes, card expirations, etc.)
```

## Protocol
- Presence in `inbox/` = unread. `mv` to `archive/` once processed — the move is the state transition.
- **Ask-first**: do not auto-drain the inbox on boot. If files are present, ask first.
- Filename shape: `<sender>.<scope>.<YYYY-MM-DD>.md`

Full canon: `/home/hruzam/reposoma/raw.canon/canon.mail-protocol.md`
