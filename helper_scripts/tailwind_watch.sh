#!/bin/zsh
echo "Execute this from the main folder of the app by running ./helper_scripts/tailwind_watch.sh"
npx tailwindcss -i ./src/input.css -o ./public/css/output.css --watch
