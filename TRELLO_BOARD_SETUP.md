# Moon Spot - Trello Board Setup 📋

## Board Structure

### Board Name: **Moon Spot Development**
**URL:** Create at https://trello.com/

---

## 📑 Lists (Columns)

1. **📚 Resources & Docs**
2. **🎯 Sprint 1 Backlog (Current)**
3. **🏃 In Progress**
4. **👀 Code Review**
5. **🧪 Testing**
6. **✅ Done - Sprint 1**
7. **🔮 Sprint 2 Backlog**
8. **🚀 Future Ideas**
9. **🐛 Bugs**
10. **❓ Questions / Blockers**

---

## 🎴 Cards by List

### 📚 Resources & Docs

**Card: Master Plan**
- Description: Link to MOON_SPOT_MASTER_PLAN.md
- Checklist: Review every Monday
- Labels: 📖 Documentation

**Card: 2026 Upgrade Plan**
- Description: Link to MOONSPOT_2026_UPGRADE_PLAN.md
- Labels: 📖 Documentation

**Card: Tech Stack Reference**
- Description: FastAPI, Next.js, PostgreSQL, Redis, Claude AI
- Checklist:
  - [ ] FastAPI docs: https://fastapi.tiangolo.com/
  - [ ] Next.js 15: https://nextjs.org/
  - [ ] PostgreSQL: https://www.postgresql.org/
  - [ ] Claude API: https://docs.anthropic.com/
- Labels: 📖 Documentation

**Card: Development Environment Setup**
- Description: How to set up local dev environment
- Checklist:
  - [ ] Install Docker Desktop
  - [ ] Install Node.js 20+
  - [ ] Install Python 3.12+
  - [ ] Install PostgreSQL 17
  - [ ] Install Redis
  - [ ] Clone repository
  - [ ] Set up API keys (Anthropic)
- Labels: 🛠️ Setup

---

### 🎯 Sprint 1 Backlog (Current) - WEEK 1

**Card: [BACKEND] Create moonspot-backend-v2 Package Structure**
- Priority: 🔴 Critical
- Story Points: 3
- Assignee: Backend Dev
- Description: Set up new FastAPI package in Buildroot
- Checklist:
  - [ ] Create `package/batocera/moonspot/moonspot-backend-v2/` directory
  - [ ] Create `moonspot-backend-v2.mk` Makefile
  - [ ] Add to `Config.in`
  - [ ] Create basic project structure
  - [ ] Add to build configuration
- Labels: 🔧 Backend, 🎯 Sprint 1
- Due Date: Day 2

**Card: [BACKEND] Set Up FastAPI Project**
- Priority: 🔴 Critical
- Story Points: 5
- Assignee: Backend Dev
- Description: Initialize FastAPI application with best practices
- Checklist:
  - [ ] Create `main.py` with FastAPI app
  - [ ] Set up CORS middleware
  - [ ] Add health check endpoint
  - [ ] Configure logging
  - [ ] Add exception handlers
  - [ ] Set up environment config
  - [ ] Create requirements.txt
- Dependencies: Create moonspot-backend-v2 Package Structure
- Labels: 🔧 Backend, 🎯 Sprint 1
- Due Date: Day 2

**Card: [DATABASE] PostgreSQL Setup & Configuration**
- Priority: 🔴 Critical
- Story Points: 5
- Assignee: Backend Dev
- Description: Set up PostgreSQL database with SQLAlchemy
- Checklist:
  - [ ] Add PostgreSQL to Buildroot packages
  - [ ] Create database models (`models/`)
  - [ ] Set up SQLAlchemy async engine
  - [ ] Create Alembic migrations setup
  - [ ] Design schema (config, roms, players, achievements, logs)
  - [ ] Create initial migration
  - [ ] Add database connection pool
  - [ ] Test connection
- Labels: 🗄️ Database, 🎯 Sprint 1
- Due Date: Day 3

**Card: [DATABASE] Redis Cache Setup**
- Priority: 🟡 High
- Story Points: 3
- Assignee: Backend Dev
- Description: Set up Redis for caching and sessions
- Checklist:
  - [ ] Add Redis to Buildroot packages
  - [ ] Create Redis client wrapper
  - [ ] Set up connection pool
  - [ ] Add cache decorators
  - [ ] Configure TTL strategies
  - [ ] Test cache operations
- Labels: 🗄️ Database, 🎯 Sprint 1
- Due Date: Day 3

**Card: [BACKEND] Authentication System (JWT)**
- Priority: 🟡 High
- Story Points: 5
- Assignee: Backend Dev
- Description: Implement JWT-based authentication
- Checklist:
  - [ ] Install python-jose and passlib
  - [ ] Create User model
  - [ ] Create authentication endpoints (/login, /refresh)
  - [ ] Implement password hashing
  - [ ] Add JWT token generation
  - [ ] Create auth dependencies
  - [ ] Add protected route decorator
  - [ ] Test authentication flow
- Dependencies: PostgreSQL Setup
- Labels: 🔧 Backend, 🔐 Security, 🎯 Sprint 1
- Due Date: Day 4

**Card: [BACKEND] Migrate Config Endpoints**
- Priority: 🟡 High
- Story Points: 3
- Assignee: Backend Dev
- Description: Migrate /api/config endpoints from Flask to FastAPI
- Checklist:
  - [ ] GET /api/config
  - [ ] POST /api/config
  - [ ] Add input validation (Pydantic)
  - [ ] Migrate data from JSON to PostgreSQL
  - [ ] Add tests
  - [ ] Update API docs
- Dependencies: PostgreSQL Setup, Authentication System
- Labels: 🔧 Backend, 🎯 Sprint 1
- Due Date: Day 5

**Card: [BACKEND] Migrate ROM Management Endpoints**
- Priority: 🟡 High
- Story Points: 5
- Assignee: Backend Dev
- Description: Migrate all ROM-related endpoints to FastAPI
- Checklist:
  - [ ] GET /api/roms/month/:id
  - [ ] POST /api/roms/upload
  - [ ] GET /api/roms/download/:id
  - [ ] POST /api/roms/activate/:id
  - [ ] Add file upload validation
  - [ ] Update ROM manager script integration
  - [ ] Add tests
  - [ ] Update API docs
- Dependencies: PostgreSQL Setup
- Labels: 🔧 Backend, 🎯 Sprint 1
- Due Date: Day 5

**Card: [BACKEND] Migrate Kiosk Settings Endpoints**
- Priority: 🟡 High
- Story Points: 3
- Assignee: Backend Dev
- Description: Migrate kiosk mode endpoints
- Checklist:
  - [ ] GET /api/settings/kiosk
  - [ ] POST /api/settings/kiosk
  - [ ] Add validation
  - [ ] Test chattr integration
  - [ ] Add tests
- Dependencies: PostgreSQL Setup
- Labels: 🔧 Backend, 🎯 Sprint 1
- Due Date: Day 6

**Card: [BACKEND] Migrate RetroAchievements Endpoints**
- Priority: 🟢 Medium
- Story Points: 3
- Assignee: Backend Dev
- Description: Migrate achievements configuration endpoints
- Checklist:
  - [ ] GET /api/achievements/config
  - [ ] POST /api/achievements/config
  - [ ] Add credential encryption
  - [ ] Add tests
- Dependencies: PostgreSQL Setup
- Labels: 🔧 Backend, 🎯 Sprint 1
- Due Date: Day 6

**Card: [BACKEND] Migrate System Control Endpoints**
- Priority: 🟢 Medium
- Story Points: 2
- Assignee: Backend Dev
- Description: Migrate reboot/shutdown endpoints
- Checklist:
  - [ ] POST /api/system/reboot
  - [ ] POST /api/system/shutdown
  - [ ] Add safety confirmations
  - [ ] Add tests
- Dependencies: PostgreSQL Setup
- Labels: 🔧 Backend, 🎯 Sprint 1
- Due Date: Day 6

**Card: [BACKEND] WebSocket Support for Real-Time Updates**
- Priority: 🟢 Medium
- Story Points: 5
- Assignee: Backend Dev
- Description: Add WebSocket endpoints for live updates
- Checklist:
  - [ ] Set up WebSocket route
  - [ ] Create connection manager
  - [ ] Add player count broadcasting
  - [ ] Add achievement notifications
  - [ ] Add ROM activation events
  - [ ] Add system status updates
  - [ ] Test WebSocket connections
- Labels: 🔧 Backend, 🎯 Sprint 1
- Due Date: Day 7

**Card: [AI] Set Up Anthropic Claude API Client**
- Priority: 🔴 Critical
- Story Points: 3
- Assignee: Backend Dev / AI Specialist
- Description: Initialize Claude API integration
- Checklist:
  - [ ] Install anthropic SDK
  - [ ] Create API client wrapper
  - [ ] Set up API key configuration
  - [ ] Create prompt templates
  - [ ] Add error handling
  - [ ] Test basic completion
- Labels: 🤖 AI, 🎯 Sprint 1
- Due Date: Day 5

**Card: [AI] Natural Language Command Parser**
- Priority: 🟡 High
- Story Points: 8
- Assignee: Backend Dev / AI Specialist
- Description: Build AI agent for natural language commands
- Checklist:
  - [ ] Create POST /api/ai/chat endpoint
  - [ ] Design system prompt for Moon Spot commands
  - [ ] Implement command extraction
  - [ ] Map commands to API calls
  - [ ] Add conversation history
  - [ ] Handle multi-turn conversations
  - [ ] Add example commands:
    - "Show me the most popular games"
    - "Activate ROMs for next month"
    - "What's the high score on Pac-Man?"
    - "Reboot the kiosk"
  - [ ] Add voice input support (Whisper)
  - [ ] Test accuracy
- Dependencies: Set Up Claude API Client
- Labels: 🤖 AI, 🎯 Sprint 1
- Due Date: Day 7

**Card: [AI] Smart ROM Recommendations**
- Priority: 🟢 Medium
- Story Points: 5
- Assignee: AI Specialist
- Description: AI-powered ROM selection recommendations
- Checklist:
  - [ ] Create GET /api/ai/recommend-roms endpoint
  - [ ] Collect player engagement data
  - [ ] Design recommendation prompt
  - [ ] Analyze play patterns
  - [ ] Generate themed ROM sets
  - [ ] Return recommendations with reasoning
  - [ ] Test recommendation quality
- Dependencies: Natural Language Command Parser, Analytics data
- Labels: 🤖 AI, 🎯 Sprint 1
- Due Date: Day 7

---

### 🎯 Sprint 1 Backlog (Current) - WEEK 2

**Card: [FRONTEND] Initialize Next.js 15 Project**
- Priority: 🔴 Critical
- Story Points: 5
- Assignee: Frontend Dev
- Description: Set up Next.js application with TypeScript
- Checklist:
  - [ ] Create Next.js 15 project with TypeScript
  - [ ] Configure Tailwind CSS 4
  - [ ] Install shadcn/ui components
  - [ ] Set up project structure (`/app`, `/components`, `/lib`)
  - [ ] Configure environment variables
  - [ ] Set up ESLint + Prettier
  - [ ] Create base layout
  - [ ] Test dev server
- Labels: 🎨 Frontend, 🎯 Sprint 1
- Due Date: Day 8

**Card: [FRONTEND] Set Up State Management & API Client**
- Priority: 🔴 Critical
- Story Points: 3
- Assignee: Frontend Dev
- Description: Configure Zustand and TanStack Query
- Checklist:
  - [ ] Install Zustand
  - [ ] Install TanStack Query v5
  - [ ] Create API client (Axios/Fetch)
  - [ ] Set up React Query provider
  - [ ] Create auth store (Zustand)
  - [ ] Create WebSocket hook
  - [ ] Add error handling
- Labels: 🎨 Frontend, 🎯 Sprint 1
- Due Date: Day 9

**Card: [FRONTEND] Authentication Flow**
- Priority: 🔴 Critical
- Story Points: 5
- Assignee: Frontend Dev
- Description: Build login page and auth flow
- Checklist:
  - [ ] Create login page
  - [ ] Build login form (React Hook Form + Zod)
  - [ ] Implement JWT storage
  - [ ] Add auth interceptor
  - [ ] Create protected route wrapper
  - [ ] Add logout functionality
  - [ ] Test authentication
- Dependencies: Backend Authentication System
- Labels: 🎨 Frontend, 🔐 Security, 🎯 Sprint 1
- Due Date: Day 9

**Card: [FRONTEND] Dashboard Layout & Navigation**
- Priority: 🟡 High
- Story Points: 5
- Assignee: Frontend Dev
- Description: Build main dashboard shell
- Checklist:
  - [ ] Create responsive sidebar
  - [ ] Add navigation menu
  - [ ] Build header with user menu
  - [ ] Add breadcrumbs
  - [ ] Create dashboard grid layout
  - [ ] Add dark/light mode toggle
  - [ ] Make mobile-responsive
  - [ ] Add loading states
- Labels: 🎨 Frontend, 🎯 Sprint 1
- Due Date: Day 10

**Card: [FRONTEND] Real-Time Status Widgets**
- Priority: 🟡 High
- Story Points: 5
- Assignee: Frontend Dev
- Description: Build live dashboard widgets
- Checklist:
  - [ ] Create system status widget (CPU, RAM, disk)
  - [ ] Create player count widget (live via WebSocket)
  - [ ] Create current game widget
  - [ ] Create uptime widget
  - [ ] Add real-time updates
  - [ ] Add loading skeletons
  - [ ] Add error states
- Dependencies: Dashboard Layout, WebSocket Support
- Labels: 🎨 Frontend, 🎯 Sprint 1
- Due Date: Day 11

**Card: [FRONTEND] ROM Management Interface**
- Priority: 🟡 High
- Story Points: 8
- Assignee: Frontend Dev
- Description: Build ROM upload and management UI
- Checklist:
  - [ ] Create ROM manager page
  - [ ] Build month selector (calendar view)
  - [ ] Add drag-and-drop file upload
  - [ ] Show upload progress bar
  - [ ] Display ROM package list
  - [ ] Add activate ROM button
  - [ ] Show current active ROM set
  - [ ] Add ROM package metadata display
  - [ ] Add delete confirmation modal
  - [ ] Test file upload flow
- Dependencies: Backend ROM Management Endpoints
- Labels: 🎨 Frontend, 🎯 Sprint 1
- Due Date: Day 12

**Card: [FRONTEND] Kiosk Settings Panel**
- Priority: 🟢 Medium
- Story Points: 3
- Assignee: Frontend Dev
- Description: Build kiosk configuration interface
- Checklist:
  - [ ] Create settings page
  - [ ] Add kiosk mode toggle
  - [ ] Add screensaver timeout setting
  - [ ] Add SSH enable/disable toggle
  - [ ] Show current kiosk status
  - [ ] Add save button with confirmation
  - [ ] Add reset to defaults
  - [ ] Test settings persistence
- Dependencies: Backend Kiosk Endpoints
- Labels: 🎨 Frontend, 🎯 Sprint 1
- Due Date: Day 12

**Card: [FRONTEND] RetroAchievements Configuration**
- Priority: 🟢 Medium
- Story Points: 3
- Assignee: Frontend Dev
- Description: Build achievements settings form
- Checklist:
  - [ ] Create achievements config page
  - [ ] Add enable/disable toggle
  - [ ] Add username/password fields
  - [ ] Add test connection button
  - [ ] Show current achievement stats
  - [ ] Add save button
  - [ ] Mask password input
  - [ ] Test configuration flow
- Dependencies: Backend Achievements Endpoints
- Labels: 🎨 Frontend, 🎯 Sprint 1
- Due Date: Day 12

**Card: [FRONTEND] AI Chat Interface**
- Priority: 🔴 Critical
- Story Points: 8
- Assignee: Frontend Dev
- Description: Build conversational AI assistant
- Checklist:
  - [ ] Create chat panel (sidebar or modal)
  - [ ] Build message list component
  - [ ] Add message input with auto-resize
  - [ ] Implement streaming responses
  - [ ] Add voice input button (Web Speech API)
  - [ ] Show typing indicator
  - [ ] Add suggested commands/prompts
  - [ ] Add conversation history
  - [ ] Add clear chat button
  - [ ] Style with chat bubbles
  - [ ] Test AI responses
- Dependencies: Backend AI Endpoints
- Labels: 🎨 Frontend, 🤖 AI, 🎯 Sprint 1
- Due Date: Day 13

**Card: [FRONTEND] System Control Panel**
- Priority: 🟢 Medium
- Story Points: 2
- Assignee: Frontend Dev
- Description: Build reboot/shutdown controls
- Checklist:
  - [ ] Create system control section
  - [ ] Add reboot button with confirmation
  - [ ] Add shutdown button with confirmation
  - [ ] Add countdown timer before action
  - [ ] Add cancel option
  - [ ] Test control flow
- Dependencies: Backend System Endpoints
- Labels: 🎨 Frontend, 🎯 Sprint 1
- Due Date: Day 13

**Card: [DOCKER] Development Environment Setup**
- Priority: 🔴 Critical
- Story Points: 5
- Assignee: DevOps / Backend Dev
- Description: Create Docker Compose for local development
- Checklist:
  - [ ] Create `docker-compose.yml`
  - [ ] Add PostgreSQL service
  - [ ] Add Redis service
  - [ ] Add FastAPI backend service
  - [ ] Add Next.js frontend service (dev mode)
  - [ ] Add environment variable templates
  - [ ] Create volume mounts for code
  - [ ] Add health checks
  - [ ] Write README for Docker setup
  - [ ] Test complete stack startup
- Labels: 🐳 DevOps, 🎯 Sprint 1
- Due Date: Day 14

**Card: [TESTING] API Integration Tests**
- Priority: 🟡 High
- Story Points: 5
- Assignee: Backend Dev
- Description: Write comprehensive API tests
- Checklist:
  - [ ] Set up pytest
  - [ ] Add test database fixtures
  - [ ] Test authentication flow
  - [ ] Test ROM management endpoints
  - [ ] Test kiosk settings endpoints
  - [ ] Test achievements endpoints
  - [ ] Test system control endpoints
  - [ ] Test WebSocket connections
  - [ ] Test AI chat endpoint
  - [ ] Achieve > 80% coverage
- Labels: 🧪 Testing, 🎯 Sprint 1
- Due Date: Day 14

**Card: [TESTING] Frontend E2E Tests**
- Priority: 🟢 Medium
- Story Points: 3
- Assignee: Frontend Dev
- Description: Write E2E tests for critical flows
- Checklist:
  - [ ] Set up Playwright or Cypress
  - [ ] Test login flow
  - [ ] Test ROM upload and activation
  - [ ] Test settings changes
  - [ ] Test AI chat interaction
  - [ ] Test mobile responsive views
- Labels: 🧪 Testing, 🎯 Sprint 1
- Due Date: Day 14

**Card: [DOCS] API Documentation**
- Priority: 🟢 Medium
- Story Points: 2
- Assignee: Backend Dev
- Description: Document all API endpoints
- Checklist:
  - [ ] Verify OpenAPI/Swagger docs are auto-generated
  - [ ] Add endpoint descriptions
  - [ ] Add request/response examples
  - [ ] Document authentication
  - [ ] Add error code reference
  - [ ] Test interactive API docs at /docs
- Labels: 📖 Documentation, 🎯 Sprint 1
- Due Date: Day 14

**Card: [DOCS] Deployment Guide**
- Priority: 🟡 High
- Story Points: 3
- Assignee: DevOps
- Description: Write guide for deploying to production
- Checklist:
  - [ ] Docker deployment steps
  - [ ] Environment variables reference
  - [ ] Database migration guide
  - [ ] Reverse proxy setup (Nginx/Caddy)
  - [ ] SSL certificate setup
  - [ ] Security best practices
  - [ ] Backup procedures
  - [ ] Troubleshooting section
- Labels: 📖 Documentation, 🎯 Sprint 1
- Due Date: Day 14

---

### 🔮 Sprint 2 Backlog (Future)

**Card: [MOBILE] Initialize React Native Project**
- Priority: 🟡 High
- Story Points: 5
- Labels: 📱 Mobile, 🔮 Sprint 2

**Card: [MOBILE] Build Main Dashboard Screen**
- Priority: 🟡 High
- Story Points: 8
- Labels: 📱 Mobile, 🔮 Sprint 2

**Card: [MOBILE] Push Notifications Setup**
- Priority: 🟡 High
- Story Points: 5
- Labels: 📱 Mobile, 🔮 Sprint 2

**Card: [ANALYTICS] Set Up TimescaleDB**
- Priority: 🟡 High
- Story Points: 5
- Labels: 📊 Analytics, 🔮 Sprint 2

**Card: [ANALYTICS] Configure Grafana Dashboards**
- Priority: 🟡 High
- Story Points: 8
- Labels: 📊 Analytics, 🔮 Sprint 2

**Card: [ANALYTICS] Player Engagement Tracking**
- Priority: 🟡 High
- Story Points: 8
- Labels: 📊 Analytics, 🔮 Sprint 2

---

### 🚀 Future Ideas

**Card: Voice Commands (Whisper API)**
- Description: Full voice control for admin panel
- Labels: 🤖 AI, 🚀 Future

**Card: AI-Generated Signage Content**
- Description: Auto-generate promotional videos
- Labels: 🤖 AI, 📺 Signage, 🚀 Future

**Card: Tournament System**
- Description: Automated tournaments with brackets
- Labels: 🏆 Features, 🚀 Future

**Card: Cloud Fleet Management**
- Description: Manage multiple kiosks from cloud
- Labels: ☁️ Cloud, 🚀 Future

**Card: Player Profiles & Social**
- Description: User accounts, friends, challenges
- Labels: 👥 Social, 🚀 Future

**Card: QR Code Check-In**
- Description: Players scan QR to track progress
- Labels: 🏆 Features, 🚀 Future

**Card: Blockchain Achievements (NFTs)**
- Description: Mint achievements as NFTs
- Labels: ⛓️ Blockchain, 🚀 Future

---

### 🐛 Bugs
*Empty for now - populate as bugs are found*

---

### ❓ Questions / Blockers
*Empty for now - populate as questions arise*

---

## 🏷️ Labels to Create

### By Type
- 🔧 Backend
- 🎨 Frontend
- 📱 Mobile
- 🗄️ Database
- 🤖 AI
- 🐳 DevOps
- 🧪 Testing
- 📖 Documentation
- 🔐 Security
- 📊 Analytics
- 📺 Signage
- 👥 Social
- 🏆 Features
- ☁️ Cloud
- ⛓️ Blockchain

### By Priority
- 🔴 Critical
- 🟡 High
- 🟢 Medium
- 🔵 Low

### By Sprint
- 🎯 Sprint 1
- 🔮 Sprint 2
- 🚀 Future

### By Status
- ✅ Done
- 🏃 In Progress
- 👀 Review
- 🧪 Testing
- ❌ Blocked

---

## 👥 Team Members to Add

1. **Backend Developer**
   - Assigned to: Backend, Database, AI cards
   
2. **Frontend Developer**
   - Assigned to: Frontend, UI/UX cards
   
3. **Mobile Developer** (Sprint 2)
   - Assigned to: Mobile app cards
   
4. **DevOps Engineer**
   - Assigned to: Docker, CI/CD, deployment cards
   
5. **AI Specialist**
   - Assigned to: AI integration cards

---

## 📊 Power-Ups to Enable (Optional)

1. **GitHub** - Link PRs to cards
2. **Slack** - Get notifications
3. **Calendar** - View due dates
4. **Custom Fields** - Add story points
5. **Card Aging** - Highlight stale cards
6. **Voting** - Team prioritization

---

## 🎯 Sprint Ceremonies

### Daily Standup (Async on Trello)
- Comment on your card: "Working on X, blocked by Y"
- Move cards through columns

### Sprint Planning (Day 1)
- Review backlog
- Assign cards
- Set story points
- Commit to sprint goal

### Sprint Review (Day 14)
- Demo completed features
- Move cards to Done
- Collect feedback

### Sprint Retrospective (Day 14)
- What went well?
- What can improve?
- Action items for next sprint

---

## 🚀 Quick Start

1. **Create Trello Board:** https://trello.com/
2. **Copy this structure** to your board
3. **Create all lists** (columns)
4. **Add all cards** from this document
5. **Create labels** with emojis
6. **Invite team members**
7. **Start Sprint 1!**

---

## 📈 Tracking Metrics

### Velocity
- Track story points completed per sprint
- Sprint 1 baseline: TBD
- Target: Increase 10% per sprint

### Burndown
- Track remaining story points daily
- Identify blockers early
- Adjust sprint scope if needed

### Cycle Time
- Time from "In Progress" to "Done"
- Target: < 3 days per card
- Identify bottlenecks

---

**Ready to start?** Create the board and let's ship Sprint 1! 🚀
