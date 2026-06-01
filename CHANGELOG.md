# Stone Paper Scissors - Changelog

## Version 4.0 (Current)

**Release Date:** 1 Jun 2026

### Major Features:

* Introduced **Quarzion AI** opponent.
* Added **DecisionEngine v1.0**.
* AI records and analyzes player move history.
* Frequency-based move prediction system.
* Counter-move generation system.
* Weighted decision making to reduce predictability.
* AI activation after sufficient gameplay data is collected.
* Added game reset functionality.

### Improvements:

* Refactored game logic into modular components.
* Separated AI logic from GUI/game management.
* Improved maintainability and future expandability.
* Significantly increased gameplay difficulty.

### Notes:

* Quarzion AI currently uses frequency analysis.
* Future versions will include behavioral tracking and persistent player profiles.
* The background image has been changed from bg.gif to bg.png
* The icon has also been changed

## Version 3.0
**Release Date:** 14 Jan 2026

### New Features:
- Full **GUI implementation** using Tkinter.
- Custom **1000x1000 canvas** with background image.
- **Game icon** support.
- User-friendly **scoreboard** for Player vs Computer.
- Game **messages** displayed dynamically (Win/Tie/Lose).
- Styled **buttons** for Stone, Paper, Scissors with colors and fonts.

### Improvements:
- Replaced CLI version with GUI version.
- Enhanced visual appeal and user interaction.
- Clean layout for labels, scores, and buttons.

### Notes:
- Ties add **0.5 points** to both players.
- Buttons and labels are customizable for colors and fonts.
- Background image (`bg.gif`) should be placed in the project folder.

---

## Version 2.1
**Release Date:** 29 Dec 2025

- CLI-based gameplay with user vs computer.
- Score tracking in console.
- Random computer choice.
- Basic win/tie/lose messages.

---

## Version 1.0
- Initial version (CLI only).
- Basic Stone Paper Scissors game.