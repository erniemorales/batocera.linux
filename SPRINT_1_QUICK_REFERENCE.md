# Sprint 1 - Quick Reference Card 🚀

**Duration:** 2 weeks (14 days)  
**Goal:** Modernize backend to FastAPI + Add AI features + Build Next.js admin dashboard  
**Team:** 1-2 developers  
**Story Points:** 95 total

---

## 📅 Timeline at a Glance

### Week 1: Backend + AI (7 days)
- **Days 1-2:** FastAPI setup, PostgreSQL, Redis
- **Days 3-4:** Authentication, database models
- **Days 5-6:** Migrate all API endpoints
- **Day 7:** Claude AI integration, WebSocket

### Week 2: Frontend (7 days)
- **Days 8-9:** Next.js setup, auth flow
- **Days 10-11:** Dashboard layout, real-time widgets
- **Days 12-13:** ROM manager, AI chat interface
- **Day 14:** Testing, Docker, documentation

---

## ✅ Daily Checklist

### Day 1 (Monday)
- [ ] Set up development environment
  - [ ] Install Docker Desktop
  - [ ] Install Node.js 20+
  - [ ] Install Python 3.12+
  - [ ] Clone repo and create feature branch
  - [ ] Get Anthropic API key
- [ ] Create moonspot-backend-v2 package structure
- [ ] Initialize FastAPI project
- [ ] Set up basic health check endpoint
- [ ] Test FastAPI server runs

**Deliverable:** FastAPI server responding to /api/health

---

### Day 2 (Tuesday)
- [ ] Add PostgreSQL to project
  - [ ] Install PostgreSQL 17
  - [ ] Create database: `moonspot_db`
  - [ ] Design schema (config, roms, players, logs)
- [ ] Set up SQLAlchemy async
- [ ] Create database models
- [ ] Create initial Alembic migration
- [ ] Test database connection

**Deliverable:** Database models created and tested

---

### Day 3 (Wednesday)
- [ ] Set up Redis
  - [ ] Install Redis 7.x
  - [ ] Create Redis client wrapper
  - [ ] Add connection pool
  - [ ] Test cache operations
- [ ] Create authentication system
  - [ ] Install python-jose, passlib
  - [ ] Create User model
  - [ ] Implement password hashing
  - [ ] Create /api/auth/login endpoint
  - [ ] Create /api/auth/refresh endpoint
  - [ ] Add JWT token generation

**Deliverable:** Working login endpoint with JWT

---

### Day 4 (Thursday)
- [ ] Add auth middleware
  - [ ] Create auth dependencies
  - [ ] Add protected route decorator
  - [ ] Test authentication flow
- [ ] Start API migration
  - [ ] Migrate GET /api/config
  - [ ] Migrate POST /api/config
  - [ ] Add Pydantic validation models
  - [ ] Test endpoints with Postman/cURL

**Deliverable:** Config endpoints migrated and working

---

### Day 5 (Friday)
- [ ] Continue API migration
  - [ ] Migrate GET /api/roms/month/:id
  - [ ] Migrate POST /api/roms/upload (with file handling)
  - [ ] Migrate GET /api/roms/download/:id
  - [ ] Migrate POST /api/roms/activate/:id
  - [ ] Test file upload with large ROM packages
- [ ] Set up Anthropic Claude API
  - [ ] Install anthropic SDK
  - [ ] Create API client wrapper
  - [ ] Test basic completion
  - [ ] Create prompt templates

**Deliverable:** ROM endpoints working + Claude API connected

---

### Day 6 (Saturday)
- [ ] Finish API migration
  - [ ] Migrate GET /api/settings/kiosk
  - [ ] Migrate POST /api/settings/kiosk
  - [ ] Migrate GET /api/achievements/config
  - [ ] Migrate POST /api/achievements/config
  - [ ] Migrate POST /api/system/reboot
  - [ ] Migrate POST /api/system/shutdown
- [ ] Add API documentation
  - [ ] Verify Swagger UI at /docs
  - [ ] Add endpoint descriptions
  - [ ] Add examples

**Deliverable:** All Flask endpoints migrated to FastAPI

---

### Day 7 (Sunday)
- [ ] Add WebSocket support
  - [ ] Create WebSocket route /ws
  - [ ] Implement connection manager
  - [ ] Add real-time event broadcasting
  - [ ] Test WebSocket connection
- [ ] Build AI chat endpoint
  - [ ] Create POST /api/ai/chat
  - [ ] Implement conversation history
  - [ ] Map natural language to API calls
  - [ ] Test example commands:
    - "Show me the most popular games"
    - "Activate next month's ROMs"
    - "What's the current high score?"
  - [ ] Add streaming responses

**Deliverable:** Real-time updates working + AI chat responding

---

### Day 8 (Monday - Week 2)
- [ ] Initialize Next.js 15 project
  - [ ] Create new Next.js app with TypeScript
  - [ ] Install Tailwind CSS 4
  - [ ] Install shadcn/ui components
  - [ ] Set up project structure
  - [ ] Configure ESLint + Prettier
  - [ ] Create base layout
  - [ ] Test dev server

**Deliverable:** Next.js app running with Tailwind

---

### Day 9 (Tuesday)
- [ ] Set up state management
  - [ ] Install Zustand
  - [ ] Install TanStack Query v5
  - [ ] Create API client (axios)
  - [ ] Set up React Query provider
  - [ ] Create auth store
  - [ ] Create WebSocket hook
- [ ] Build authentication flow
  - [ ] Create login page
  - [ ] Build login form (React Hook Form + Zod)
  - [ ] Implement JWT storage
  - [ ] Add auth interceptor
  - [ ] Create protected route wrapper
  - [ ] Test login flow

**Deliverable:** Login working, JWT stored, auth flow complete

---

### Day 10 (Wednesday)
- [ ] Build dashboard layout
  - [ ] Create responsive sidebar
  - [ ] Add navigation menu
  - [ ] Build header with user menu
  - [ ] Create dashboard grid layout
  - [ ] Add dark/light mode toggle
  - [ ] Make mobile-responsive
  - [ ] Add loading states

**Deliverable:** Dashboard shell with navigation

---

### Day 11 (Thursday)
- [ ] Build real-time status widgets
  - [ ] System status widget (CPU, RAM, disk)
  - [ ] Player count widget (WebSocket)
  - [ ] Current game widget
  - [ ] Uptime widget
  - [ ] Connect to WebSocket
  - [ ] Test real-time updates
  - [ ] Add loading skeletons

**Deliverable:** Live dashboard with real-time data

---

### Day 12 (Friday)
- [ ] Build ROM management interface
  - [ ] Create ROM manager page
  - [ ] Build month selector
  - [ ] Add drag-and-drop file upload
  - [ ] Show upload progress
  - [ ] Display ROM package list
  - [ ] Add activate button
  - [ ] Show current active ROM set
  - [ ] Test file upload
- [ ] Build kiosk settings panel
  - [ ] Add kiosk mode toggle
  - [ ] Add screensaver timeout
  - [ ] Add SSH toggle
  - [ ] Test settings save

**Deliverable:** ROM upload working, settings configurable

---

### Day 13 (Saturday)
- [ ] Build AI chat interface
  - [ ] Create chat panel (sidebar or modal)
  - [ ] Build message list
  - [ ] Add message input
  - [ ] Implement streaming responses
  - [ ] Add voice input button (Web Speech API)
  - [ ] Add suggested commands
  - [ ] Style with chat bubbles
  - [ ] Test AI interaction
- [ ] Build achievements config
  - [ ] Create config form
  - [ ] Add username/password fields
  - [ ] Test connection button
  - [ ] Test save

**Deliverable:** AI chat working with voice input

---

### Day 14 (Sunday - Sprint End)
- [ ] Docker development environment
  - [ ] Create docker-compose.yml
  - [ ] Add PostgreSQL service
  - [ ] Add Redis service
  - [ ] Add FastAPI service
  - [ ] Add Next.js service
  - [ ] Test full stack startup
- [ ] Testing
  - [ ] Write API integration tests (pytest)
  - [ ] Write frontend E2E tests (Playwright)
  - [ ] Achieve > 80% backend coverage
  - [ ] Test critical flows
- [ ] Documentation
  - [ ] Update API docs
  - [ ] Write deployment guide
  - [ ] Update README
- [ ] Sprint review
  - [ ] Demo all features
  - [ ] Collect feedback
  - [ ] Plan Sprint 2

**Deliverable:** Complete Sprint 1, ready for deployment

---

## 🎯 Sprint Goal

**By end of Sprint 1, we will have:**
1. ✅ FastAPI backend (3x faster than Flask)
2. ✅ PostgreSQL database (replacing JSON files)
3. ✅ Redis caching layer
4. ✅ JWT authentication
5. ✅ All API endpoints migrated
6. ✅ WebSocket real-time updates
7. ✅ Claude AI natural language commands
8. ✅ Next.js modern admin dashboard
9. ✅ Mobile-responsive UI
10. ✅ AI chat interface with voice input
11. ✅ Docker development environment
12. ✅ Comprehensive tests
13. ✅ Updated documentation

---

## 📦 Tech Stack

### Backend
```
FastAPI 0.115+
PostgreSQL 17
Redis 7.x
SQLAlchemy 2.0 (async)
Pydantic V2
python-jose (JWT)
Anthropic SDK (Claude API)
```

### Frontend
```
Next.js 15
React 19
TypeScript 5
Tailwind CSS 4
shadcn/ui
Zustand
TanStack Query v5
Socket.io-client
React Hook Form
Zod
```

---

## 🚀 Getting Started Commands

### Backend Setup
```bash
# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy asyncpg redis anthropic python-jose passlib python-multipart

# Run FastAPI
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

### Frontend Setup
```bash
# Create Next.js app
npx create-next-app@latest moonspot-admin --typescript --tailwind --app

# Install dependencies
npm install zustand @tanstack/react-query axios socket.io-client
npm install react-hook-form zod @hookform/resolvers

# Add shadcn/ui
npx shadcn-ui@latest init
npx shadcn-ui@latest add button input card dialog

# Run dev server
npm run dev
```

### Database Setup
```bash
# Start PostgreSQL
docker run --name moonspot-postgres -e POSTGRES_PASSWORD=moonspot -p 5432:5432 -d postgres:17

# Create database
psql -h localhost -U postgres -c "CREATE DATABASE moonspot_db;"

# Run migrations
alembic upgrade head
```

### Redis Setup
```bash
# Start Redis
docker run --name moonspot-redis -p 6379:6379 -d redis:7
```

---

## 🧪 Testing Commands

### Backend Tests
```bash
pytest tests/ -v --cov=app --cov-report=html
```

### Frontend Tests
```bash
npm run test
npm run test:e2e
```

---

## 📊 Success Metrics

At end of Sprint 1, we should have:
- [ ] API response time < 100ms (p95)
- [ ] Frontend load time < 2s
- [ ] WebSocket latency < 500ms
- [ ] AI command accuracy > 85%
- [ ] Test coverage > 80%
- [ ] Zero critical bugs
- [ ] All features demo-ready

---

## 🆘 Getting Help

### Resources
- FastAPI docs: https://fastapi.tiangolo.com/
- Next.js docs: https://nextjs.org/docs
- Claude API: https://docs.anthropic.com/
- PostgreSQL: https://www.postgresql.org/docs/

### Blockers
If blocked, create a card in "Questions / Blockers" Trello list with:
- Description of issue
- What you've tried
- Error messages
- Screenshots

---

## 💡 Pro Tips

1. **Commit often** - At least 2-3 commits per day
2. **Test as you go** - Don't wait until Day 14
3. **Use the AI** - Ask Claude for help with code
4. **Stay focused** - Don't add features outside Sprint 1 scope
5. **Take breaks** - Avoid burnout
6. **Ask questions** - Better to ask than guess
7. **Document** - Update docs as you code
8. **Review daily** - Check progress against this checklist

---

## 🎉 Demo Checklist (Day 14)

Prepare to demo these flows:
- [ ] Login to admin dashboard
- [ ] View real-time dashboard stats
- [ ] Upload ROM package for a month
- [ ] Activate ROM package
- [ ] Change kiosk settings
- [ ] Configure RetroAchievements
- [ ] Chat with AI: "Show me top games"
- [ ] Use voice command
- [ ] View on mobile device
- [ ] Reboot system (in demo mode)

---

**Let's ship this! 🚀**

Print this out, check items daily, and track progress on Trello.
