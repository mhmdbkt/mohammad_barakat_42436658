#!/usr/bin/env bash
set -e

# Next.js app (frontend) if missing
if [ ! -f "frontend/package.json" ]; then
  npx --yes create-next-app@latest frontend --use-npm --eslint --src-dir --app --no-tailwind --ts
fi

# Django project if missing
if [ ! -d "backend/django_app" ]; then
  mkdir -p backend
  cd backend
  django-admin startproject django_app
  cd ..
fi

mkdir -p .mongo/data
echo "post-create complete"
