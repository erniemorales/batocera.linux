# Moon Spot - Complete Project Plan 🌙

> **Note:** Moon Spot is a branded variant of Batocera Linux. All Moon Spot packages are **optional add-ons** that do not affect the core Batocera project. This is a downstream derivative maintained separately.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Vision & Strategy](#vision--strategy)
3. [Current Status](#current-status)
4. [2026 Upgrade Plan](#2026-upgrade-plan)
5. [Implementation Roadmap](#implementation-roadmap)
6. [Sprint 1: Quick Wins (2 Weeks)](#sprint-1-quick-wins-2-weeks)
7. [Daily Execution Guide](#daily-execution-guide)
8. [Trello Board Structure](#trello-board-structure)
9. [Tech Stack](#tech-stack)
10. [Budget & Resources](#budget--resources)
11. [Success Metrics](#success-metrics)
12. [Risk Management](#risk-management)
13. [Next Steps](#next-steps)

---

## Project Overview

### What is Moon Spot?

Moon Spot is a **branded version of Batocera Linux** designed specifically for arcade kiosk deployments. It builds on Batocera's solid foundation and adds:

- 🤖 AI-powered management (Claude 5, natural language commands)
- 📱 Mobile app for remote management
- 📊 Advanced analytics and player engagement tracking
- 🎮 Monthly ROM rotation system with backend management
- 🏆 High score tracking via RetroAchievements
- 📺 Intelligent digital signage for promotional content
- ☁️ Optional cloud fleet management for multi-kiosk operations

### Relationship to Batocera

```
Batocera Linux (Upstream)
    ↓
    ├── Core Batocera (unchanged)
    └── Moon Spot Packages (optional add-ons)
        ├── moonspot-splash
        ├── moonspot-kiosk
        ├── moonspot-backend
        ├── moonspot-signage
        └── moonspot-backend-v2 (planned)
```

**Important:**
- Moon Spot packages are **BR2_EXTERNAL** add-ons
- Do NOT modify core Batocera packages
- Can be built as separate configuration: `batocera-moonspot-x86_64`
- Regular Batocera builds are unaffected
- All Moon Spot code lives in `package/batocera/moonspot/`

### Target Market

- Arcade bars and gaming lounges
- Retro gaming cafes
- Corporate break rooms
- Hotel gaming rooms
- Event spaces and conventions
- Esports venues with retro gaming areas

---

## Vision & Strategy

### Mission Statement

Transform arcade kiosk management by combining retro gaming nostalgia with cutting-edge AI technology, making it dead simple to deploy and manage engaging gaming experiences at scale.

### Unique Selling Points (USPs)

1. **AI-Powered Everything**
   - Talk to your kiosk: "Show me the most popular games"
   - Automated ROM curation based on player engagement
   - Smart analytics and predictive recommendations

2. **Mobile-First Management**
   - Manage kiosks from your phone
   - Push notifications for achievements and alerts
   - Multi-kiosk fleet control from one dashboard

3. **Plug-and-Play Deployment**
   - Flash USB and go
   - Auto-configuration
   - Zero-touch deployment

4. **Mac Compatible**
   - Works on old MacBook Pros (A1226 and newer)
   - Breathe life into legacy hardware
   - Nouveau driver support for old NVIDIA GPUs

5. **Open Source + Premium Options**
   - Free self-hosted version (forever)
   - Optional cloud services for fleet management
   - No vendor lock-in

### Strategic Positioning

**Tagline:** "The Future of Retro Gaming"

**Brand Identity:**
- Primary Color: Electric purple (#667eea)
- Secondary Color: Deep violet (#764ba2)
- Accent: Neon cyan (#00f5ff)
- Style: Retro-futuristic, nostalgic but modern
- Logo: Moon with game controller, glowing spot/beacon

---

## Current Status

### Phase 0: Foundation ✅ COMPLETE

**Completed Deliverables:**
- ✅ Base Moon Spot packages (4 packages)
  - `moonspot-splash` - Custom branding and splash screens
  - `moonspot-kiosk` - Kiosk mode and ROM manager
  - `moonspot-backend` - Flask API (v1)
  - `moonspot-signage` - Digital signage system
- ✅ Flask REST API backend
- ✅ Basic HTML/CSS/JS admin interface
- ✅ ROM rotation system with monthly packages
- ✅ RetroAchievements integration
- ✅ Mac compatibility (GeForce 8600M GT via Nouveau)
- ✅ Complete documentation (English + Spanish)
- ✅ Board configuration: `batocera-moonspot-x86_64`

**Current Tech Stack:**
- Backend: Flask (Python 3)
- Frontend: Vanilla HTML/CSS/JavaScript
- Database: JSON files
- Video: MPV for digital signage
- Auth: None (basic access)

**Current Limitations:**
- No real-time updates
- No mobile app
- No AI features
- No proper database
- No authentication
- Limited analytics
- Manual ROM management

### What We're Building Next

**Phase 1: Quick Wins (Sprint 1)** ← **WE ARE HERE**
- Modernize to FastAPI + PostgreSQL + Next.js
- Add Claude AI for natural language commands
- Real-time WebSocket updates
- Modern responsive admin dashboard
- Voice command support

---

## 2026 Upgrade Plan

### Overview of All Upgrades

| # | Upgrade | Priority | Timeline | Cost |
|---|---------|----------|----------|------|
| 1 | AI Integration (Claude 5) | 🔴 Critical | Sprint 1 | $50-150/mo |
| 2 | FastAPI Backend | 🔴 Critical | Sprint 1 | Free |
| 3 | Next.js Frontend | 🔴 Critical | Sprint 1 | Free |
| 4 | PostgreSQL + Redis | 🔴 Critical | Sprint 1 | Free |
| 5 | Mobile App (React Native) | 🟡 High | Sprint 2 | Free (dev) |
| 6 | Advanced Analytics | 🟡 High | Sprint 2 | Free |
| 7 | Cloud Integration | 🟢 Medium | Sprint 3 | $10-50/mo |
| 8 | Voice Control | 🟢 Medium | Sprint 3 | $10-30/mo |
| 9 | Social Features | 🟢 Medium | Sprint 3 | Free |
| 10 | Enhanced Signage (AI) | 🔵 Low | Sprint 4 | $10-30/mo |

### Detailed Upgrade Descriptions

#### 1. AI-Powered Intelligence Layer ⭐

**Features:**
- Natural language admin interface
  - "Show me the most popular games this month"
  - "Create a ROM rotation for retro platformers"
  - "What's the high score on Pac-Man?"
- Smart ROM curation (analyze player engagement)
- AI-generated digital signage content
- Voice commands via Whisper API
- Intelligent player assistance chatbot
- Difficulty adjustment recommendations

**Tech:** Claude 5 / Opus 4.8, Whisper API  
**Cost:** ~$50-200/month (API usage)  
**Timeline:** Sprint 1 (Week 1, Days 5-7)

#### 2. Modern Backend Architecture ⭐

**Upgrade:** Flask → FastAPI + PostgreSQL + Redis

**Why FastAPI:**
- 3x faster than Flask
- Async support for real-time features
- Auto-generated API documentation (OpenAPI/Swagger)
- Type safety with Pydantic
- Better WebSocket support

**Why PostgreSQL:**
- Proper relational database (vs JSON files)
- ACID compliance
- Advanced analytics queries
- Scalability
- TimescaleDB extension for metrics

**Why Redis:**
- Real-time features (pub/sub)
- Session management
- API response caching
- Rate limiting
- WebSocket state management

**Cost:** Free (open source)  
**Timeline:** Sprint 1 (Week 1, Days 1-6)

#### 3. Next-Gen Frontend ⭐

**Upgrade:** Vanilla HTML → Next.js 15 + React 19 + Tailwind CSS 4

**Features:**
- Server-Side Rendering (SSR) for instant loads
- Real-time dashboard with live data
- Progressive Web App (PWA) - install on any device
- Dark/Light mode
- Mobile-first responsive design
- Offline support for basic admin tasks
- Modern component library (shadcn/ui)

**Cost:** Free (open source)  
**Timeline:** Sprint 1 (Week 2, Days 8-13)

#### 4. Mobile Management App 📱

**Platform:** React Native (Expo) for iOS + Android

**Features:**
- Remote kiosk management
- Push notifications (achievements, alerts)
- QR code scanning for setup
- Offline mode with sync
- Biometric authentication
- Multi-kiosk dashboard
- ROM upload from mobile
- System health monitoring

**Cost:**
- Development: Free
- App Store: $99/year (Apple) + $25 one-time (Google)
- Push notifications: Free (Firebase)

**Timeline:** Sprint 2 (Weeks 3-4)

#### 5. Advanced Analytics & Telemetry 📊

**Features:**
- Player engagement metrics (session duration, popular games)
- Hardware monitoring (CPU, RAM, disk, temperature)
- Predictive analytics (AI-powered ROM recommendations)
- Real-time dashboards (Grafana)
- Alerting system (Prometheus)

**Tech:** PostgreSQL + TimescaleDB + Grafana + Prometheus  
**Cost:** Free (open source)  
**Timeline:** Sprint 2 (Weeks 3-4)

#### 6. Cloud Integration ☁️

**Features:**
- Cloud dashboard for all kiosks
- Remote configuration management
- Centralized ROM repository
- Automatic backups
- Fleet management (10+ kiosks)
- A/B testing framework

**Deployment Options:**
- Self-hosted VPS: $5-20/month
- Serverless (Vercel + Supabase): Free tier available
- Managed cloud (AWS/GCP): $50-200/month

**Timeline:** Sprint 4 (Weeks 8-9)

#### 7. Voice Control & Accessibility 🎤

**Features:**
- Voice commands for admin panel
- Speech-to-text (Whisper API)
- Text-to-speech (ElevenLabs API)
- Natural language processing (Claude)
- Screen reader support
- High contrast mode
- Keyboard-only navigation

**Cost:** ~$10-30/month (API usage)  
**Timeline:** Sprint 3 (Weeks 5-7)

#### 8. Social & Community Features 👥

**Features:**
- Player profiles with avatars
- Friend system
- Global leaderboards
- Challenges and tournaments
- Social sharing (Twitter, Discord)
- Achievement showcase
- Highlight reel generation

**Cost:** Free  
**Timeline:** Sprint 3 (Weeks 5-7)

#### 9. Enhanced Digital Signage 🎥

**Features:**
- AI-generated promotional videos
- Smart content rotation
- Player presence detection
- Interactive QR codes
- Live leaderboards with animations
- Social media integration

**Tech:** Chromium kiosk mode, HTML5, Claude API, Stability AI  
**Cost:** ~$10-30/month (image generation)  
**Timeline:** Sprint 3 (Weeks 5-7)

---

## Implementation Roadmap

### Complete Timeline (10 Weeks)

```
Phase 0: Foundation [COMPLETE ✅]
   └── Base packages, Flask API, basic UI

Phase 1: Quick Wins ⚡ [CURRENT - Weeks 1-2]
   ├── Week 1: FastAPI + PostgreSQL + AI
   └── Week 2: Next.js frontend + testing

Phase 2: Mobile & Analytics 📱 [Weeks 3-4]
   ├── Week 3: React Native app foundation
   └── Week 4: Analytics + push notifications

Phase 3: Advanced Features 🚀 [Weeks 5-7]
   ├── Week 5: Voice control + social features
   ├── Week 6: Tournament system
   └── Week 7: Enhanced signage

Phase 4: Cloud & Scale ☁️ [Weeks 8-9]
   ├── Week 8: Cloud infrastructure
   └── Week 9: Fleet management

Phase 5: Polish & Launch 🎨 [Week 10]
   └── Documentation, security audit, marketing
```

---

## Sprint 1: Quick Wins (2 Weeks)

### Sprint Goal

**Modernize the core tech stack and add AI-powered features**

By end of Sprint 1, we will have:
1. ✅ FastAPI backend (3x faster)
2. ✅ PostgreSQL database
3. ✅ Redis caching layer
4. ✅ JWT authentication
5. ✅ All API endpoints migrated
6. ✅ WebSocket real-time updates
7. ✅ Claude AI natural language interface
8. ✅ Next.js modern admin dashboard
9. ✅ Mobile-responsive UI
10. ✅ AI chat with voice input
11. ✅ Docker dev environment
12. ✅ Comprehensive tests

### Sprint Metrics

| Metric | Value |
|--------|-------|
| Duration | 14 days |
| Story Points | 95 total |
| Tasks | 33 cards |
| Team Size | 1-2 developers |
| Budget | $20/month (Claude API) |

### Week 1: Backend Modernization + AI

**Focus:** FastAPI, PostgreSQL, Redis, Authentication, Claude AI

**Days 1-2: Foundation**
- Create moonspot-backend-v2 package structure
- Set up FastAPI project with proper structure
- Configure PostgreSQL 17 + SQLAlchemy async
- Design database schema
- Set up Redis for caching

**Days 3-4: Authentication & Core APIs**
- Implement JWT authentication
- Create User model and auth endpoints
- Add password hashing (bcrypt)
- Migrate config endpoints from Flask
- Add Pydantic validation models

**Days 5-6: API Migration**
- Migrate ROM management endpoints
- Migrate kiosk settings endpoints
- Migrate RetroAchievements endpoints
- Migrate system control endpoints
- Add comprehensive error handling

**Day 7: Real-Time + AI**
- Add WebSocket support for live updates
- Set up Anthropic Claude API client
- Build natural language command parser
- Implement AI chat endpoint with streaming
- Add voice input support (Whisper)

**Deliverables:**
- ✅ Fully functional FastAPI backend
- ✅ All Flask endpoints migrated
- ✅ Database with proper schema
- ✅ Redis caching working
- ✅ JWT authentication implemented
- ✅ AI chat responding to commands
- ✅ WebSocket real-time updates

### Week 2: Frontend Modernization

**Focus:** Next.js, React, Tailwind CSS, shadcn/ui

**Days 8-9: Foundation**
- Initialize Next.js 15 + TypeScript project
- Configure Tailwind CSS 4
- Install shadcn/ui components
- Set up Zustand state management
- Configure TanStack Query for API calls
- Build authentication flow (login page)

**Days 10-11: Dashboard**
- Create responsive dashboard layout
- Build navigation sidebar
- Add real-time status widgets
- Connect WebSocket for live updates
- Add dark/light mode toggle
- Make mobile-responsive

**Days 12-13: Feature Pages + AI**
- Build ROM management interface (upload, activate)
- Create kiosk settings panel
- Build RetroAchievements configuration
- Add system control panel (reboot/shutdown)
- Build AI chat interface with voice input
- Add suggested commands and conversation history

**Day 14: Testing + Docker**
- Write API integration tests (pytest)
- Write frontend E2E tests (Playwright)
- Create Docker Compose for dev environment
- Update documentation
- Sprint review and demo

**Deliverables:**
- ✅ Modern Next.js admin dashboard
- ✅ All features implemented
- ✅ Mobile-responsive UI
- ✅ AI chat interface working
- ✅ Docker dev environment
- ✅ Tests passing (>80% coverage)

---

## Daily Execution Guide

### Day 1 (Monday - Week 1) 🚀

**Goal:** Set up FastAPI foundation

**Tasks:**
- [ ] Install development tools
  - [ ] Docker Desktop
  - [ ] Node.js 20+
  - [ ] Python 3.12+
  - [ ] PostgreSQL 17
  - [ ] Redis 7
- [ ] Get Anthropic API key from https://console.anthropic.com/
- [ ] Create feature branch: `git checkout -b moonspot/sprint-1-modernization`
- [ ] Create package directory:
  ```bash
  mkdir -p package/batocera/moonspot/moonspot-backend-v2/api
  cd package/batocera/moonspot/moonspot-backend-v2/api
  ```
- [ ] Initialize Python environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install fastapi uvicorn sqlalchemy asyncpg redis anthropic python-jose passlib
  ```
- [ ] Create `main.py` with FastAPI app and health endpoint
- [ ] Test server: `uvicorn main:app --reload --port 8080`
- [ ] Verify health check: `curl http://localhost:8080/api/health`

**Deliverable:** FastAPI server responding to /api/health ✅

---

### Day 2 (Tuesday)

**Goal:** Database setup and schema design

**Tasks:**
- [ ] Start PostgreSQL:
  ```bash
  docker run --name moonspot-postgres \
    -e POSTGRES_PASSWORD=moonspot \
    -e POSTGRES_DB=moonspot_db \
    -p 5432:5432 -d postgres:17
  ```
- [ ] Create database models in `models/` directory:
  - [ ] `config.py` - System configuration
  - [ ] `roms.py` - ROM packages and metadata
  - [ ] `players.py` - Player profiles and stats
  - [ ] `achievements.py` - RetroAchievements data
  - [ ] `logs.py` - System and audit logs
  - [ ] `users.py` - Admin users
- [ ] Set up SQLAlchemy async engine in `database.py`
- [ ] Install Alembic: `pip install alembic`
- [ ] Initialize migrations: `alembic init alembic`
- [ ] Create initial migration: `alembic revision --autogenerate -m "Initial schema"`
- [ ] Run migration: `alembic upgrade head`
- [ ] Test database connection with simple query

**Deliverable:** Database models created and migrated ✅

---

### Day 3 (Wednesday)

**Goal:** Redis setup + Authentication system

**Tasks:**
- [ ] Start Redis:
  ```bash
  docker run --name moonspot-redis -p 6379:6379 -d redis:7
  ```
- [ ] Create Redis client wrapper in `cache.py`
- [ ] Add cache decorators for API responses
- [ ] Install auth dependencies: `pip install python-jose[cryptography] passlib[bcrypt]`
- [ ] Create User model (if not done Day 2)
- [ ] Implement password hashing utilities
- [ ] Create authentication endpoints:
  - [ ] `POST /api/auth/login` - Returns JWT token
  - [ ] `POST /api/auth/refresh` - Refresh token
  - [ ] `POST /api/auth/logout` - Invalidate token
- [ ] Create auth dependency for protected routes
- [ ] Test login flow with Postman/cURL

**Deliverable:** JWT authentication working ✅

---

### Day 4 (Thursday)

**Goal:** Start API migration from Flask

**Tasks:**
- [ ] Create Pydantic models for validation in `schemas/`
- [ ] Migrate config endpoints:
  - [ ] `GET /api/config` - Get current configuration
  - [ ] `POST /api/config` - Update configuration
- [ ] Add authentication to endpoints (`Depends(get_current_user)`)
- [ ] Migrate data from JSON files to PostgreSQL:
  ```bash
  python scripts/migrate_json_to_postgres.py
  ```
- [ ] Test endpoints with authentication headers
- [ ] Verify data persistence in PostgreSQL
- [ ] Check auto-generated docs at http://localhost:8080/docs

**Deliverable:** Config endpoints migrated ✅

---

### Day 5 (Friday)

**Goal:** ROM management + Claude API setup

**Tasks:**
- [ ] Migrate ROM endpoints:
  - [ ] `GET /api/roms/month/:id` - Get ROM manifest
  - [ ] `POST /api/roms/upload` - Upload ROM package with file validation
  - [ ] `GET /api/roms/download/:id` - Download ROM package
  - [ ] `POST /api/roms/activate/:id` - Activate ROM set
- [ ] Add file upload validation (max size, file type)
- [ ] Test large ROM package upload
- [ ] Set up Anthropic SDK:
  ```bash
  pip install anthropic
  ```
- [ ] Create `ai/claude_client.py` wrapper
- [ ] Test basic completion:
  ```python
  from anthropic import Anthropic
  client = Anthropic(api_key="your-key")
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Say hello"}]
  )
  print(message.content)
  ```
- [ ] Create prompt templates in `ai/prompts.py`

**Deliverable:** ROM endpoints working + Claude API connected ✅

---

### Day 6 (Saturday)

**Goal:** Complete API migration

**Tasks:**
- [ ] Migrate kiosk settings endpoints:
  - [ ] `GET /api/settings/kiosk`
  - [ ] `POST /api/settings/kiosk`
- [ ] Migrate RetroAchievements endpoints:
  - [ ] `GET /api/achievements/config`
  - [ ] `POST /api/achievements/config`
- [ ] Add credential encryption for RA password
- [ ] Migrate system control endpoints:
  - [ ] `POST /api/system/reboot`
  - [ ] `POST /api/system/shutdown`
- [ ] Add safety confirmations for destructive actions
- [ ] Write API integration tests in `tests/`:
  ```bash
  pip install pytest pytest-asyncio httpx
  pytest tests/ -v
  ```
- [ ] Update OpenAPI docs with descriptions and examples

**Deliverable:** All Flask endpoints migrated ✅

---

### Day 7 (Sunday)

**Goal:** WebSocket + AI chat

**Tasks:**
- [ ] Add WebSocket support to FastAPI
- [ ] Create WebSocket route: `ws://localhost:8080/ws`
- [ ] Implement connection manager in `websocket.py`
- [ ] Add real-time event broadcasting:
  - Player count updates
  - Achievement notifications
  - ROM activation events
  - System status changes
- [ ] Test WebSocket with JS client
- [ ] Build AI chat endpoint:
  - [ ] `POST /api/ai/chat` with streaming support
- [ ] Implement conversation history (store in Redis)
- [ ] Map natural language to API calls:
  ```python
  commands = {
      "show popular games": lambda: get_game_stats(),
      "activate roms": lambda month: activate_roms(month),
      "reboot": lambda: reboot_system()
  }
  ```
- [ ] Add example commands:
  - "Show me the most popular games"
  - "Activate ROMs for next month"
  - "What's the high score on Pac-Man?"
  - "Reboot the kiosk"
- [ ] Test AI command accuracy

**Deliverable:** Real-time updates + AI chat working ✅

**🎉 End of Week 1 - Backend Complete!**

---

### Day 8 (Monday - Week 2)

**Goal:** Next.js foundation

**Tasks:**
- [ ] Create Next.js project:
  ```bash
  cd package/batocera/moonspot/moonspot-frontend
  npx create-next-app@latest . --typescript --tailwind --app --no-git
  ```
- [ ] Install dependencies:
  ```bash
  npm install zustand @tanstack/react-query axios socket.io-client
  npm install react-hook-form zod @hookform/resolvers
  ```
- [ ] Initialize shadcn/ui:
  ```bash
  npx shadcn-ui@latest init
  npx shadcn-ui@latest add button input card dialog toast
  ```
- [ ] Set up project structure:
  ```
  app/
  ├── (auth)/
  │   └── login/
  ├── (dashboard)/
  │   ├── layout.tsx
  │   ├── page.tsx
  │   ├── roms/
  │   ├── settings/
  │   └── achievements/
  components/
  lib/
  └── hooks/
  ```
- [ ] Configure environment variables in `.env.local`
- [ ] Test dev server: `npm run dev`

**Deliverable:** Next.js app running ✅

---

### Day 9 (Tuesday)

**Goal:** State management + Authentication

**Tasks:**
- [ ] Create API client in `lib/api.ts`:
  ```typescript
  import axios from 'axios';
  const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL,
  });
  ```
- [ ] Set up TanStack Query provider in `app/providers.tsx`
- [ ] Create auth store with Zustand in `lib/store/auth.ts`
- [ ] Build login page in `app/(auth)/login/page.tsx`
- [ ] Create login form with React Hook Form + Zod validation
- [ ] Implement JWT storage (localStorage or cookies)
- [ ] Add axios interceptor for auth tokens
- [ ] Create protected route wrapper
- [ ] Add logout functionality
- [ ] Test complete auth flow

**Deliverable:** Login working, JWT persisted ✅

---

### Day 10 (Wednesday)

**Goal:** Dashboard layout

**Tasks:**
- [ ] Create dashboard layout in `app/(dashboard)/layout.tsx`
- [ ] Build responsive sidebar with navigation
- [ ] Add header with user menu and dark mode toggle
- [ ] Create breadcrumb component
- [ ] Build dashboard grid layout for widgets
- [ ] Implement dark/light mode (use next-themes)
- [ ] Make mobile-responsive with Tailwind breakpoints
- [ ] Add loading skeletons for widgets
- [ ] Test on desktop, tablet, mobile sizes

**Deliverable:** Dashboard shell complete ✅

---

### Day 11 (Thursday)

**Goal:** Real-time status widgets

**Tasks:**
- [ ] Create WebSocket hook in `lib/hooks/useWebSocket.ts`
- [ ] Build system status widget (CPU, RAM, disk usage)
- [ ] Build player count widget (real-time via WebSocket)
- [ ] Build current game widget
- [ ] Build uptime widget
- [ ] Connect all widgets to WebSocket
- [ ] Add loading states and error handling
- [ ] Style with shadcn/ui Card components
- [ ] Test real-time updates

**Deliverable:** Live dashboard with real-time data ✅

---

### Day 12 (Friday)

**Goal:** ROM manager + Settings

**Tasks:**
- [ ] Build ROM management page in `app/(dashboard)/roms/page.tsx`
- [ ] Create month selector (calendar input)
- [ ] Add drag-and-drop file upload zone:
  ```bash
  npm install react-dropzone
  ```
- [ ] Show upload progress bar
- [ ] Display ROM package list in table
- [ ] Add activate ROM button with confirmation
- [ ] Show current active ROM set
- [ ] Build kiosk settings page in `app/(dashboard)/settings/page.tsx`
- [ ] Add kiosk mode toggle switch
- [ ] Add screensaver timeout input
- [ ] Add SSH enable/disable toggle
- [ ] Test ROM upload and activation flow

**Deliverable:** ROM manager + settings working ✅

---

### Day 13 (Saturday)

**Goal:** AI chat interface

**Tasks:**
- [ ] Create AI chat component (sidebar or modal)
- [ ] Build message list with auto-scroll
- [ ] Add message input with auto-resize textarea
- [ ] Implement streaming responses from API
- [ ] Add voice input button using Web Speech API:
  ```typescript
  const recognition = new (window as any).webkitSpeechRecognition();
  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    sendMessage(transcript);
  };
  ```
- [ ] Show typing indicator while AI responds
- [ ] Add suggested commands as buttons
- [ ] Add conversation history (store in state)
- [ ] Add clear chat button
- [ ] Style chat bubbles (user vs AI)
- [ ] Build achievements config page in `app/(dashboard)/achievements/page.tsx`
- [ ] Test AI interaction end-to-end

**Deliverable:** AI chat with voice input working ✅

---

### Day 14 (Sunday - Sprint End)

**Goal:** Testing, Docker, Documentation

**Tasks:**
- [ ] Create `docker-compose.yml` in project root:
  ```yaml
  version: '3.8'
  services:
    postgres:
      image: postgres:17
      environment:
        POSTGRES_PASSWORD: moonspot
        POSTGRES_DB: moonspot_db
      ports:
        - "5432:5432"
    redis:
      image: redis:7
      ports:
        - "6379:6379"
    backend:
      build: ./package/batocera/moonspot/moonspot-backend-v2
      ports:
        - "8080:8080"
      depends_on:
        - postgres
        - redis
    frontend:
      build: ./package/batocera/moonspot/moonspot-frontend
      ports:
        - "3000:3000"
      depends_on:
        - backend
  ```
- [ ] Write backend tests:
  ```bash
  cd package/batocera/moonspot/moonspot-backend-v2
  pytest tests/ -v --cov=app --cov-report=html
  ```
- [ ] Target > 80% test coverage
- [ ] Write frontend E2E tests:
  ```bash
  cd package/batocera/moonspot/moonspot-frontend
  npm install -D @playwright/test
  npx playwright test
  ```
- [ ] Update API documentation in `moonspot-backend-v2/README.md`
- [ ] Write deployment guide in `DEPLOYMENT.md`
- [ ] Update main README with Sprint 1 changes
- [ ] Test complete stack with Docker:
  ```bash
  docker-compose up
  ```
- [ ] Sprint review: Demo all features
- [ ] Retrospective: What went well? What to improve?
- [ ] Plan Sprint 2

**Deliverable:** Sprint 1 complete, ready to deploy ✅

**🎉 Sprint 1 Done - Ready for Production!**

---

## Trello Board Structure

### Board Setup

**Board Name:** Moon Spot Development  
**URL:** https://trello.com/ (create new board)

### Lists (Columns)

1. **📚 Resources & Docs** - Links to documentation
2. **🎯 Sprint 1 Backlog** - Current sprint tasks
3. **🏃 In Progress** - Actively working on
4. **👀 Code Review** - Ready for review
5. **🧪 Testing** - In QA
6. **✅ Done - Sprint 1** - Completed tasks
7. **🔮 Sprint 2 Backlog** - Future tasks
8. **🚀 Future Ideas** - Long-term features
9. **🐛 Bugs** - Issues to fix
10. **❓ Questions / Blockers** - Need help

### Key Cards (Sprint 1)

**Week 1 Cards (17 total, 50 story points):**

1. **[BACKEND] Create moonspot-backend-v2 Package** (3 pts)
2. **[BACKEND] Set Up FastAPI Project** (5 pts)
3. **[DATABASE] PostgreSQL Setup** (5 pts)
4. **[DATABASE] Redis Cache Setup** (3 pts)
5. **[BACKEND] Authentication System (JWT)** (5 pts)
6. **[BACKEND] Migrate Config Endpoints** (3 pts)
7. **[BACKEND] Migrate ROM Endpoints** (5 pts)
8. **[BACKEND] Migrate Kiosk Settings** (3 pts)
9. **[BACKEND] Migrate Achievements** (3 pts)
10. **[BACKEND] Migrate System Control** (2 pts)
11. **[BACKEND] WebSocket Support** (5 pts)
12. **[AI] Set Up Claude API** (3 pts)
13. **[AI] Natural Language Parser** (8 pts)
14. **[AI] Smart ROM Recommendations** (5 pts)

**Week 2 Cards (16 total, 45 story points):**

15. **[FRONTEND] Initialize Next.js** (5 pts)
16. **[FRONTEND] State Management Setup** (3 pts)
17. **[FRONTEND] Authentication Flow** (5 pts)
18. **[FRONTEND] Dashboard Layout** (5 pts)
19. **[FRONTEND] Real-Time Widgets** (5 pts)
20. **[FRONTEND] ROM Management Interface** (8 pts)
21. **[FRONTEND] Kiosk Settings Panel** (3 pts)
22. **[FRONTEND] Achievements Config** (3 pts)
23. **[FRONTEND] AI Chat Interface** (8 pts)
24. **[FRONTEND] System Control Panel** (2 pts)
25. **[DOCKER] Development Environment** (5 pts)
26. **[TESTING] API Integration Tests** (5 pts)
27. **[TESTING] Frontend E2E Tests** (3 pts)
28. **[DOCS] API Documentation** (2 pts)
29. **[DOCS] Deployment Guide** (3 pts)

### Labels

**By Type:**
- 🔧 Backend
- 🎨 Frontend
- 📱 Mobile
- 🗄️ Database
- 🤖 AI
- 🐳 DevOps
- 🧪 Testing
- 📖 Documentation

**By Priority:**
- 🔴 Critical
- 🟡 High
- 🟢 Medium
- 🔵 Low

**By Sprint:**
- 🎯 Sprint 1
- 🔮 Sprint 2
- 🚀 Future

---

## Tech Stack

### Backend (Sprint 1)

```yaml
Framework: FastAPI 0.115+
Language: Python 3.12
Server: Uvicorn (ASGI)
Database: PostgreSQL 17
Cache: Redis 7.x
ORM: SQLAlchemy 2.0 (async)
Validation: Pydantic V2
Migrations: Alembic
Auth: python-jose (JWT) + passlib (bcrypt)
AI: Anthropic SDK (Claude 5)
Testing: pytest + pytest-asyncio
```

### Frontend (Sprint 1)

```yaml
Framework: Next.js 15
Language: TypeScript 5
UI Library: React 19
Styling: Tailwind CSS 4
Components: shadcn/ui + Radix UI
State: Zustand
Data Fetching: TanStack Query v5
Real-time: Socket.io-client
Forms: React Hook Form + Zod
Testing: Playwright
```

### Mobile (Sprint 2)

```yaml
Framework: React Native (Expo)
Language: TypeScript
Navigation: React Navigation 7
State: Zustand
UI: React Native Paper
Push: Firebase Cloud Messaging
Storage: SQLite + async-storage
```

### Infrastructure

```yaml
Containers: Docker + Docker Compose
Reverse Proxy: Nginx or Caddy
Monitoring: Prometheus + Grafana
Logging: Loki or ELK Stack
CI/CD: GitHub Actions
```

---

## Budget & Resources

### One-Time Costs

| Item | Cost |
|------|------|
| Apple Developer Account | $99/year |
| Google Play Developer | $25 one-time |
| Domain (moonspot.io) | $12/year |
| **Total Year 1** | **$136** |

### Monthly Operational Costs

**Tier 1: Self-Hosted (Minimal)**
- VPS (2 GB RAM): $6/month (Hetzner) or $12/month (DigitalOcean)
- Claude API (low usage): $20/month
- Domain + SSL: Free (Let's Encrypt)
- **Total: $26-32/month**

**Tier 2: Cloud Hybrid (Recommended)**
- VPS (4 GB RAM): $12-24/month
- Managed PostgreSQL: Free (Supabase) or $15/month
- Claude API (medium): $100/month
- Whisper API: $10/month
- CDN: Free (Cloudflare)
- **Total: $122-149/month**

**Tier 3: Full Cloud (Scale)**
- AWS/GCP Compute: $50/month
- Managed PostgreSQL: $50/month
- Redis Cloud: $10/month
- Claude API (high): $200/month
- Whisper + TTS: $30/month
- Grafana Cloud: $20/month
- CDN + Storage: $20/month
- **Total: $380/month**

### Development Resources

**Team Size Options:**

**Solo Developer (80 hours):**
- Week 1: Backend + AI (40 hrs)
- Week 2: Frontend (40 hrs)
- Cost: Free (your time) or $4K-8K if outsourced

**Small Team (2 devs):**
- 1 Backend + AI specialist
- 1 Frontend specialist
- Timeline: Same (2 weeks) but parallel work
- Cost: Free (if in-house) or $8K-15K if outsourced

### Required API Keys

1. **Anthropic API** (Claude) - https://console.anthropic.com/
2. **OpenAI API** (Whisper, optional) - https://platform.openai.com/
3. **Firebase** (Push notifications, Sprint 2) - https://console.firebase.google.com/

---

## Success Metrics

### Technical KPIs (Sprint 1)

| Metric | Target | How to Measure |
|--------|--------|----------------|
| API Response Time | < 100ms (p95) | Prometheus metrics |
| Frontend Load Time | < 2s | Lighthouse score |
| WebSocket Latency | < 500ms | Browser DevTools |
| Test Coverage | > 80% | pytest --cov |
| Lighthouse Score | > 90 | Chrome Lighthouse |
| AI Command Accuracy | > 85% | Manual testing |

### Business Metrics (Post-Launch)

| Metric | 3 Months | 6 Months |
|--------|----------|----------|
| Kiosks Deployed | 10+ | 50+ |
| Monthly Active Players | 500/kiosk | 1000/kiosk |
| Player Retention (Monthly) | 60% | 70% |
| Mobile App Downloads | 100+ | 1000+ |
| Cloud Customers | 3+ | 10+ |
| Average Session Time | 30 min | 45 min |

---

## Risk Management

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| API performance issues | Medium | High | Load testing, caching, CDN |
| Database scaling problems | Low | High | Proper indexing, read replicas |
| AI API costs spike | Medium | Medium | Rate limiting, response caching |
| WebSocket connection drops | Medium | Medium | Auto-reconnect, fallback polling |
| Mobile app store rejection | Low | Medium | Follow guidelines, beta test |
| Security vulnerabilities | Medium | High | Regular audits, pen testing |

### Business Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Slow market adoption | Medium | Medium | Free tier, great docs, demos |
| Competition emerges | Low | Low | First-mover, AI differentiation |
| Support burden too high | Medium | Medium | Comprehensive docs, community |
| Cloud costs unsustainable | Low | Medium | Efficient code, cost monitoring |

### Mitigation Strategies

1. **Performance:** Load test before launch, use caching extensively
2. **Security:** Regular security audits, follow OWASP top 10
3. **Costs:** Monitor API usage, set budget alerts, optimize prompts
4. **Support:** Build comprehensive docs, create community forum
5. **Quality:** High test coverage, code reviews, CI/CD pipeline

---

## Next Steps

### Immediate Actions (Today)

1. **✅ Review this plan** - Read through, ask questions
2. **🎯 Set up Trello board** - Create board, add cards (30 min)
3. **🔑 Get API keys:**
   - Anthropic: https://console.anthropic.com/
   - Create account, add payment method, generate API key
4. **💻 Set up dev environment:**
   ```bash
   # Install Docker Desktop
   # Install Node.js 20+
   # Install Python 3.12+
   ```
5. **🌿 Create feature branch:**
   ```bash
   git checkout -b moonspot/sprint-1-modernization
   ```

### Week 1 Kickoff (Day 1)

1. **Morning:**
   - Review Day 1 checklist in "Daily Execution Guide"
   - Move Day 1 cards to "In Progress" in Trello
   - Start FastAPI project setup

2. **Afternoon:**
   - Complete FastAPI health endpoint
   - Test server running
   - Commit progress

3. **Evening:**
   - Update Trello cards
   - Plan tomorrow's work
   - Get good sleep 😴

### Sprint Ceremonies

**Daily Standup (Async):**
- Update Trello card comments
- Move cards through workflow
- Flag blockers

**Sprint Planning (Day 1):**
- Review all Sprint 1 cards
- Confirm priorities
- Commit to sprint goal

**Sprint Review (Day 14):**
- Demo all completed features
- Collect feedback
- Celebrate wins 🎉

**Sprint Retrospective (Day 14):**
- What went well?
- What can improve?
- Action items for Sprint 2

---

## Appendix

### Useful Commands Reference

**Backend:**
```bash
# Start FastAPI dev server
uvicorn main:app --reload --port 8080

# Run tests
pytest tests/ -v --cov=app

# Database migrations
alembic revision --autogenerate -m "message"
alembic upgrade head

# Start PostgreSQL (Docker)
docker run --name moonspot-postgres \
  -e POSTGRES_PASSWORD=moonspot \
  -e POSTGRES_DB=moonspot_db \
  -p 5432:5432 -d postgres:17

# Start Redis (Docker)
docker run --name moonspot-redis -p 6379:6379 -d redis:7
```

**Frontend:**
```bash
# Start Next.js dev server
npm run dev

# Build for production
npm run build

# Run tests
npm test
npm run test:e2e

# Add shadcn component
npx shadcn-ui@latest add [component-name]
```

**Docker:**
```bash
# Start all services
docker-compose up

# Stop all services
docker-compose down

# Rebuild services
docker-compose up --build

# View logs
docker-compose logs -f backend
```

**Git:**
```bash
# Create feature branch
git checkout -b moonspot/feature-name

# Commit changes
git add .
git commit -m "message"

# Push to remote
git push -u origin moonspot/feature-name
```

### Learning Resources

**FastAPI:**
- Official docs: https://fastapi.tiangolo.com/
- Tutorial: https://fastapi.tiangolo.com/tutorial/

**Next.js:**
- Official docs: https://nextjs.org/docs
- Learn Next.js: https://nextjs.org/learn

**Claude API:**
- Anthropic docs: https://docs.anthropic.com/
- Prompt engineering: https://docs.anthropic.com/en/docs/prompt-engineering

**PostgreSQL:**
- Official docs: https://www.postgresql.org/docs/
- SQLAlchemy async: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html

### Support & Community

**Questions?**
- Create card in Trello "Questions / Blockers" list
- Email: morales.ernesto@gmail.com

**Future Community:**
- GitHub Discussions (post-launch)
- Discord server (post-launch)
- Documentation site (post-launch)

---

## Document Control

**Version:** 1.0  
**Last Updated:** 2026-07-16  
**Status:** Ready for Sprint 1  
**Next Review:** End of Sprint 1 (2 weeks)

**Contributors:**
- Ernesto Morales (morales.ernesto@gmail.com)
- Claude Sonnet 4.5 (AI Assistant)

**License:** GPL v3 (same as Batocera Linux)

---

**🚀 Ready to ship Sprint 1? Let's do this!**

Print this document, check off daily items, update Trello, and track progress. We've got 14 days to transform Moon Spot. Let's make it happen! 💪
