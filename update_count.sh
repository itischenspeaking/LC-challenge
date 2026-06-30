#!/bin/bash
count=$(ls -d problems/*/ 2>/dev/null | wc -l | tr -d ' ')
sed -i '' "s/^\*\*Total: .*\*\*/**Total: ${count}**/" README.md
echo "Updated: $count problems"
