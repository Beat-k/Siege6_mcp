# Siege6 Desktop Audio Reference

A desktop application that provides instant access to Rainbow Six Siege audio references during gameplay.

## Features

- **Global Hotkey**: Press `Ctrl+Shift+S` anywhere to show/hide the reference window
- **System Tray**: Minimizes to tray for zero desktop clutter
- **Quick Search**: Type to instantly filter operators and maps
- **Always-on-Top**: Window stays visible when activated
- **Comprehensive Data**: All operators and maps included
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

1. Install Node.js (v16 or higher)
2. Clone/download this repository
3. Navigate to the `desktop-app` folder
4. Run `npm install` to install dependencies
5. Run `npm start` to launch the application

## Usage

1. Launch the app - it will minimize to system tray
2. During Rainbow Six Siege gameplay, press `Ctrl+Shift+S`
3. The reference window appears instantly
4. Type to search for operators or switch between tabs
5. Click outside the window or press the hotkey again to hide

## Hotkeys

- `Ctrl+Shift+S`: Show/hide reference window
- Right-click tray icon: Access menu options

## Building

To create distributable executables:

```bash
npm run dist
```

Executables will be created in the `dist` folder.

## Data Source

Audio descriptions are based on community knowledge and official game information. The app includes all current Rainbow Six Siege operators and maps.

## Performance Impact

- Minimal system resources when minimized
- Instant activation with global hotkey
- No impact on game performance

## Troubleshooting

- **Hotkey not working**: Make sure no other applications are using `Ctrl+Shift+S`
- **Window not appearing**: Check if the app is running in system tray
- **Search not working**: Ensure you're typing in the search box

## Requirements

- Node.js >= 16
- Windows 10+, macOS 10.13+, or Linux (Ubuntu 18.04+)

## License

MIT License - See LICENSE file in parent directory