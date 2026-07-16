# Moon Spot 2026 Upgrade Plan 🚀

## Executive Summary

Modernize Moon Spot with cutting-edge 2026 technologies while maintaining the core Batocera Linux foundation. This upgrade focuses on AI integration, modern web stack, mobile support, and enhanced analytics.

---

## 🎯 Priority Upgrades

### 1. **AI-Powered Intelligence Layer** ⭐ HIGH PRIORITY

**Current State:** No AI features
**2026 Upgrade:** Claude 5 / Opus 4.8 Integration

**Features:**
- **Natural Language Admin Interface**
  - "Show me the most popular games this month"
  - "Create a ROM rotation for retro platformers"
  - Voice commands via Whisper API
  
- **Smart ROM Curation**
  - AI analyzes player engagement data
  - Suggests optimal monthly ROM selections
  - Predicts which games will be popular
  
- **AI-Generated Digital Signage Content**
  - Auto-generate promotional videos
  - Dynamic content based on current games
  - Personalized player highlights
  
- **Intelligent Player Assistance**
  - AI chatbot for game tips and help
  - Difficulty adjustment recommendations
  - Achievement guidance

**Implementation:**
```python
# New package: moonspot-ai
# Using Anthropic Claude API
- Claude 5 for natural language interface
- Computer Use for automated admin tasks
- Vision API for analyzing gameplay screenshots
```

**Cost:** ~$50-200/month (Anthropic API usage)

---

### 2. **Modern Backend Architecture** ⭐ HIGH PRIORITY

**Current:** Flask + JSON files
**Upgrade:** FastAPI + PostgreSQL + Redis

**Why:**
- **FastAPI**: Async support, 3x faster, auto-documentation, type safety
- **PostgreSQL**: Proper relational data, analytics queries, scalability
- **Redis**: Real-time features, session management, caching

**New Capabilities:**
- Real-time player counts via WebSocket
- Instant achievement notifications
- Live leaderboard updates
- Session persistence across reboots
- Advanced analytics queries
- API rate limiting and caching

**Implementation:**
```bash
# Add new packages
BR2_PACKAGE_MOONSPOT_BACKEND_V2=y
- FastAPI + Uvicorn
- PostgreSQL 17
- Redis 7.x
- SQLAlchemy 2.0 (async)
- Pydantic V2
```

**Migration Path:**
1. Run both Flask and FastAPI in parallel
2. Migrate endpoints one by one
3. Migrate data from JSON to PostgreSQL
4. Cut over completely

**Cost:** Free (open source)

---

### 3. **Next-Gen Frontend** ⭐ HIGH PRIORITY

**Current:** Vanilla HTML/CSS/JS
**Upgrade:** Next.js 15 + React 19 + Tailwind CSS 4 + shadcn/ui

**Features:**
- **Server-Side Rendering (SSR)** for instant loads
- **Real-time Dashboard** with live data
- **Progressive Web App (PWA)** - install on any device
- **Dark/Light Mode** with system preference detection
- **Mobile-First Responsive Design**
- **Offline Support** for basic admin tasks

**Components:**
- Live player dashboard with real-time stats
- Drag-and-drop ROM upload
- Visual ROM rotation calendar
- Interactive analytics charts (Chart.js / Recharts)
- AI chat interface
- Mobile-optimized touch controls

**Tech Stack:**
```json
{
  "framework": "Next.js 15.x",
  "ui": "React 19 + shadcn/ui",
  "styling": "Tailwind CSS 4.x",
  "state": "Zustand / Jotai",
  "data-fetching": "TanStack Query v5",
  "realtime": "Socket.io / Server-Sent Events",
  "charts": "Recharts / Chart.js 4",
  "forms": "React Hook Form + Zod"
}
```

**Cost:** Free (open source)

---

### 4. **Mobile Management App** 🔥 NEW FEATURE

**Platform:** React Native (iOS + Android) or Flutter
**Why:** Manage kiosks from anywhere, receive push notifications

**Features:**
- Remote kiosk management
- Push notifications for achievements and alerts
- QR code scanning for quick setup
- Offline mode with sync
- Biometric authentication
- Multi-kiosk management dashboard
- Player stats and leaderboards
- ROM upload from mobile
- System health monitoring

**Screens:**
1. Dashboard - All kiosks overview
2. Kiosk Detail - Individual machine stats
3. ROM Manager - Upload and activate ROMs
4. Players - Leaderboards and achievements
5. Analytics - Engagement metrics
6. Settings - Configuration

**Implementation:**
- React Native with Expo (recommended)
- Or Flutter for better performance
- Push notifications via Firebase Cloud Messaging
- Offline-first architecture with local SQLite

**Cost:** 
- Development: Free (open source)
- App Store fees: $99/year (Apple) + $25 one-time (Google)
- Push notifications: Free (FCM)

---

### 5. **Advanced Analytics & Telemetry** 📊

**Current:** No analytics
**Upgrade:** Comprehensive player engagement tracking

**Features:**
- **Player Engagement Metrics**
  - Session duration per game
  - Most popular games
  - Peak usage times
  - Player retention rates
  - Achievement completion rates
  
- **Hardware Monitoring**
  - CPU/GPU temperature
  - RAM usage
  - Disk space
  - Network status
  - Uptime tracking
  
- **Predictive Analytics**
  - AI-powered ROM recommendations
  - Optimal rotation timing
  - Predicted popular games
  - Maintenance forecasting

**Tech Stack:**
```yaml
Collection: Custom telemetry service
Storage: PostgreSQL + TimescaleDB
Visualization: Grafana dashboards
Alerting: Prometheus + AlertManager
AI Analysis: Claude API for insights
```

**Dashboards:**
1. **Operator Dashboard** - Real-time kiosk health
2. **Player Analytics** - Engagement and trends
3. **Revenue Analytics** (if applicable)
4. **System Performance** - Hardware metrics

**Cost:**
- TimescaleDB: Free
- Grafana: Free
- Prometheus: Free
- Hosting costs: $10-50/month (cloud deployment)

---

### 6. **Enhanced Digital Signage** 🎥

**Current:** Basic MPV video playback
**Upgrade:** AI-powered dynamic content system

**Features:**
- **AI-Generated Content**
  - Auto-generate highlight reels from gameplay
  - Create promotional videos using AI
  - Dynamic leaderboards with animations
  
- **Smart Content Rotation**
  - Time-based scheduling
  - Player presence detection (show different content when active)
  - Game-aware content (show tips for current game)
  
- **Interactive Elements**
  - QR codes for mobile app download
  - Live leaderboards
  - Social media integration
  - Real-time achievement celebrations

**Tech Stack:**
```yaml
Rendering: Chromium in kiosk mode
Content: HTML5 + CSS animations + WebGL
Video: HLS streaming for smooth playback
AI Generation: Anthropic Claude + Stability AI
Management: Web-based CMS
```

**Cost:**
- Stability AI (image generation): ~$10-30/month
- Video processing: Free (local ffmpeg)

---

### 7. **Cloud Integration & Remote Management** ☁️

**Current:** Local only
**Upgrade:** Optional cloud sync and management

**Features:**
- **Cloud Dashboard** - Manage all kiosks from one place
- **Remote Configuration** - Push settings to multiple machines
- **Cloud ROM Repository** - Centralized ROM storage and distribution
- **Automatic Backups** - Save states and configurations
- **Fleet Management** - Monitor dozens/hundreds of kiosks
- **A/B Testing** - Test ROM rotations across different locations

**Architecture:**
```
┌─────────────────────────────────────┐
│   Cloud Dashboard (Next.js)         │
│   - Multi-kiosk management          │
│   - Analytics aggregation           │
│   - ROM repository                  │
└─────────────────┬───────────────────┘
                  │ HTTPS/WebSocket
    ┌─────────────┼─────────────┐
    │             │             │
┌───▼────┐   ┌───▼────┐   ┌───▼────┐
│Kiosk 1 │   │Kiosk 2 │   │Kiosk N │
│        │   │        │   │        │
└────────┘   └────────┘   └────────┘
```

**Deployment Options:**
1. **Self-Hosted** (Free)
   - VPS with Docker
   - $5-20/month (DigitalOcean, Linode)
   
2. **Serverless** (Pay-per-use)
   - Vercel (Frontend): Free tier available
   - Supabase (Database): Free tier available
   - Cloudflare Workers (Edge functions): Free tier available
   
3. **Managed** (Enterprise)
   - AWS Amplify + RDS: ~$50-200/month
   - Google Cloud Run + Cloud SQL: ~$30-150/month

**Cost:** $0-200/month depending on scale

---

### 8. **Security & Authentication** 🔒

**Current:** No authentication
**Upgrade:** Enterprise-grade security

**Features:**
- **OAuth2 Authentication**
  - Google Sign-In
  - GitHub Sign-In
  - Microsoft Azure AD
  - Custom SSO integration
  
- **Role-Based Access Control (RBAC)**
  - Admin: Full control
  - Operator: Day-to-day management
  - Viewer: Read-only access
  - Player: Leaderboard and stats only
  
- **API Security**
  - JWT tokens with rotation
  - Rate limiting (1000 requests/hour per user)
  - API key authentication for integrations
  - CORS configuration
  - HTTPS enforcement
  
- **Audit Logging**
  - Track all configuration changes
  - ROM upload/activation history
  - Login attempts and access logs
  - Export logs for compliance

**Implementation:**
```python
# FastAPI with OAuth2
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
import passlib

# Libraries
- python-jose (JWT)
- passlib (password hashing)
- python-multipart (file uploads)
- slowapi (rate limiting)
```

**Cost:** Free (open source libraries)

---

### 9. **Voice Control & Accessibility** 🎤

**Current:** None
**Upgrade:** Voice-controlled admin interface

**Features:**
- **Voice Commands**
  - "Activate next month's ROMs"
  - "Show me the top 5 games this week"
  - "Reboot kiosk 3"
  - "What's the current high score on Pac-Man?"
  
- **Accessibility**
  - Screen reader support
  - High contrast mode
  - Keyboard-only navigation
  - Text-to-speech for notifications
  - Voice feedback for player actions

**Tech Stack:**
```yaml
Speech-to-Text: OpenAI Whisper API
Text-to-Speech: ElevenLabs API or OpenAI TTS
Natural Language: Claude 5 API
Frontend: Web Speech API (browser support)
```

**Cost:** ~$10-30/month (API usage)

---

### 10. **Social & Community Features** 👥

**Current:** Individual play only
**Upgrade:** Social arcade experience

**Features:**
- **Player Profiles**
  - Avatars and usernames
  - Stat tracking across all games
  - Personal achievement showcase
  - Friend system
  
- **Leaderboards 2.0**
  - Global leaderboards
  - Friends-only leaderboards
  - Daily/Weekly/Monthly/All-time
  - Per-game and overall rankings
  
- **Challenges & Tournaments**
  - Create custom challenges
  - Monthly tournaments with prizes
  - Head-to-head competitions
  - Time-limited events
  
- **Social Sharing**
  - Share achievements to Twitter/X
  - Screenshot sharing with auto-watermark
  - Highlight reel generation
  - QR codes for profile viewing

**Implementation:**
```yaml
Backend: FastAPI + PostgreSQL
Authentication: OAuth2 (social login)
Real-time: WebSocket for live updates
Sharing: Twitter API, Discord webhooks
Notifications: Web Push API
```

**Cost:** Free (mostly)

---

## 📦 Implementation Packages

### New Buildroot Packages

```
package/batocera/moonspot/
├── moonspot-ai/                    # AI integration
│   ├── anthropic-sdk.mk
│   └── scripts/moonspot-ai-agent
├── moonspot-backend-v2/           # FastAPI backend
│   ├── fastapi.mk
│   ├── postgresql.mk
│   ├── redis.mk
│   └── api/moonspot-api-v2.py
├── moonspot-frontend/             # Next.js frontend
│   ├── nextjs.mk
│   └── web/                       # React app
├── moonspot-analytics/            # Analytics engine
│   ├── timescaledb.mk
│   ├── grafana.mk
│   └── prometheus.mk
└── moonspot-mobile/               # Mobile app (optional)
    └── build-artifacts/
```

---

## 🚀 Migration Roadmap

### Phase 1: Foundation (Month 1)
- ✅ Set up new FastAPI backend alongside Flask
- ✅ Set up PostgreSQL + Redis
- ✅ Create database schema
- ✅ Migrate core endpoints to FastAPI
- ✅ Add authentication (JWT + OAuth2)

### Phase 2: Frontend Modernization (Month 2)
- ✅ Build Next.js frontend
- ✅ Implement real-time dashboard
- ✅ Add mobile responsiveness
- ✅ Integrate with FastAPI backend
- ✅ Deploy as PWA

### Phase 3: AI Integration (Month 3)
- ✅ Add Claude API integration
- ✅ Implement natural language interface
- ✅ Add smart ROM recommendations
- ✅ Implement voice commands
- ✅ Add AI-powered analytics

### Phase 4: Mobile App (Month 4)
- ✅ Build React Native app
- ✅ Implement core features
- ✅ Add push notifications
- ✅ Beta testing
- ✅ App store deployment

### Phase 5: Analytics & Advanced Features (Month 5)
- ✅ Set up TimescaleDB for metrics
- ✅ Configure Grafana dashboards
- ✅ Add player engagement tracking
- ✅ Implement predictive analytics
- ✅ Add social features

### Phase 6: Cloud & Scaling (Month 6)
- ✅ Set up cloud infrastructure
- ✅ Implement fleet management
- ✅ Add multi-kiosk support
- ✅ Performance optimization
- ✅ Load testing and deployment

---

## 💰 Cost Summary

### One-Time Costs
| Item | Cost |
|------|------|
| Apple Developer Account | $99/year |
| Google Play Developer Account | $25 one-time |
| Domain name (moonspot.io) | $12/year |
| **Total Year 1** | **$136** |

### Monthly Costs (Optional Services)

| Service | Free Tier | Paid (Recommended) |
|---------|-----------|-------------------|
| **AI APIs (Claude + Whisper)** | - | $50-150/month |
| **Cloud Hosting (VPS)** | - | $10-50/month |
| **Database (Managed PostgreSQL)** | Supabase free tier | $25/month |
| **CDN (Cloudflare)** | Free | Free-$20/month |
| **Text-to-Speech (ElevenLabs)** | 10K chars/month | $11-99/month |
| **Monitoring (Grafana Cloud)** | Free tier | $8-49/month |
| **Total Monthly** | **~$0** | **$104-368/month** |

### Cost-Saving Options
1. **Self-Hosted Everything**: $0/month (use free tier services)
2. **Basic Cloud**: $60-100/month (essential services only)
3. **Full Featured**: $200-400/month (all premium features)
4. **Enterprise**: $500+/month (multi-location, high availability)

**Recommendation:** Start with self-hosted ($0/month), scale to Basic Cloud as you grow.

---

## 🎨 Tech Stack Summary

### Backend
```yaml
Primary: FastAPI 0.115+ (Python 3.12)
Database: PostgreSQL 17 + TimescaleDB
Cache: Redis 7.x
Message Queue: Redis Streams
API Docs: Automatic (FastAPI OpenAPI)
Authentication: OAuth2 + JWT
ORM: SQLAlchemy 2.0 (async)
Validation: Pydantic V2
```

### Frontend
```yaml
Framework: Next.js 15 + React 19
Styling: Tailwind CSS 4.x
Components: shadcn/ui + Radix UI
State: Zustand / Jotai
Data Fetching: TanStack Query v5
Real-time: Socket.io / SSE
Charts: Recharts / Chart.js
Forms: React Hook Form + Zod
PWA: next-pwa
```

### Mobile
```yaml
Framework: React Native (Expo)
Navigation: React Navigation 7
State: Zustand
API: TanStack Query
Push: Firebase Cloud Messaging
Storage: SQLite + async-storage
UI: React Native Paper / Tamagui
```

### Infrastructure
```yaml
Containers: Docker + Docker Compose
Reverse Proxy: Nginx / Caddy
Monitoring: Prometheus + Grafana
Logging: Loki / ELK Stack
CI/CD: GitHub Actions
Deployment: Docker Swarm / K8s (optional)
```

### AI & ML
```yaml
LLM: Claude 5 / Opus 4.8 (Anthropic)
Speech-to-Text: Whisper API (OpenAI)
Text-to-Speech: ElevenLabs / OpenAI TTS
Image Generation: Stability AI (optional)
Analytics: Custom ML models (scikit-learn)
```

---

## 📊 Success Metrics

### Technical KPIs
- API response time < 100ms (p95)
- Frontend load time < 2s
- Mobile app startup < 1s
- 99.9% uptime
- Real-time updates < 500ms latency

### Business KPIs
- Player engagement time +50%
- Monthly active users tracking
- Achievement completion rate +30%
- ROM rotation efficiency +40%
- Operator time savings 60%

---

## 🔄 Backward Compatibility

All upgrades maintain backward compatibility:
- Old Flask API available during transition
- JSON config files auto-migrated to PostgreSQL
- Existing ROM packages supported
- No breaking changes to kiosk behavior
- Gradual rollout with feature flags

---

## 🎯 Quick Wins (Implement First)

1. **FastAPI Backend** (1 week)
   - Immediate 3x performance boost
   - Better error handling
   - Auto-generated API docs
   
2. **Next.js Frontend** (2 weeks)
   - Modern, responsive UI
   - Much better UX
   - PWA support
   
3. **Claude AI Chat** (3 days)
   - Natural language admin commands
   - Instant wow factor
   - Easy to implement

4. **Real-time Dashboard** (1 week)
   - Live player counts
   - Instant notifications
   - WebSocket integration

---

## 📝 Next Steps

1. **Review this plan** - Confirm priorities and budget
2. **Choose deployment model** - Self-hosted vs. cloud
3. **Set timeline** - 3-month MVP or 6-month full rollout
4. **Start with Phase 1** - FastAPI backend + PostgreSQL
5. **Parallel frontend work** - Begin Next.js development
6. **Testing environment** - Set up staging kiosk

---

## 🤝 Support & Development

**Want to start implementing?** I can help you:
1. Set up the FastAPI backend right now
2. Create the Next.js frontend scaffolding
3. Integrate Claude AI for natural language control
4. Build the mobile app foundation
5. Set up Docker development environment

**Which upgrade would you like to start with?**
