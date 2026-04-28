from app.database import SessionLocal
from app.models import Day
from app.database import Base, engine

db = SessionLocal()

Base.metadata.create_all(bind=engine)

# Clear old data (optional but recommended)
db.query(Day).delete()

days_data = [

# 🟢 DAYS 1–14 (Foundation)
(1, "Setup Python, VS Code, basic syntax (lists, dicts)", "Foundation"),
(2, "Functions, loops, JSON handling, API calls", "Foundation"),
(3, "Install FastAPI, create /hello endpoint", "Foundation"),
(4, "Request/response handling, POST endpoint", "Foundation"),
(5, "Setup OpenAI API, first API call", "Foundation"),
(6, "Build /ask-ai endpoint (LLM response)", "Foundation"),
(7, "Add system prompts, experiment with prompts", "Foundation"),
(8, "Connect React frontend to backend", "Foundation"),
(9, "Add conversation memory using Postgres", "Foundation"),
(10, "Improve chat UI (chat bubbles, loaders)", "Foundation"),
(11, "Add error handling and logging", "Foundation"),
(12, "Deploy backend on GCP Cloud Run", "Foundation"),
(13, "Deploy frontend (Vercel/Firebase)", "Foundation"),
(14, "Polish project, README, GitHub push", "Foundation"),

# 🟡 DAYS 15–45 (RAG)
(15, "Learn embeddings (concept)", "RAG"),
(16, "Setup LangChain and FAISS", "RAG"),
(17, "Load and split documents into chunks", "RAG"),
(18, "Generate embeddings", "RAG"),
(19, "Store embeddings in vector DB", "RAG"),
(20, "Build retrieval system", "RAG"),
(21, "Connect retrieval with LLM (basic RAG)", "RAG"),
(22, "Add PDF upload feature (part 1)", "RAG"),
(23, "Complete PDF upload feature", "RAG"),
(24, "Improve answers via prompt tuning", "RAG"),
(25, "Refine prompt quality", "RAG"),
(26, "Support multiple documents", "RAG"),
(27, "Enhance multi-doc retrieval", "RAG"),
(28, "Add metadata filtering", "RAG"),
(29, "Improve filtering logic", "RAG"),
(30, "Build UI for document Q&A", "RAG"),
(31, "Add authentication (JWT)", "RAG"),
(32, "Secure APIs + auth testing", "RAG"),
(33, "Optimize response time", "RAG"),
(34, "Parallel processing improvements", "RAG"),
(35, "Add logging system", "RAG"),
(36, "Monitoring + debugging tools", "RAG"),
(37, "Dockerize backend", "RAG"),
(38, "Dockerize full system", "RAG"),
(39, "Deploy on GCP (part 1)", "RAG"),
(40, "Deploy full system (part 2)", "RAG"),
(41, "Test with real documents", "RAG"),
(42, "Fix bugs from testing", "RAG"),
(43, "Polish UI + backend", "RAG"),
(44, "Prepare demo video", "RAG"),
(45, "Push final project to GitHub", "RAG"),

# 🔴 DAYS 46–75 (SaaS)
(46, "Choose SaaS idea (resume analyzer/support bot)", "SaaS"),
(47, "Design system architecture", "SaaS"),
(48, "Finalize DB schema + APIs", "SaaS"),
(49, "Build backend APIs (part 1)", "SaaS"),
(50, "Build backend APIs (part 2)", "SaaS"),
(51, "Continue backend services", "SaaS"),
(52, "Finalize backend", "SaaS"),
(53, "Start frontend UI (React)", "SaaS"),
(54, "Build frontend components", "SaaS"),
(55, "Connect frontend to backend", "SaaS"),
(56, "Complete UI flows", "SaaS"),
(57, "Integrate LLM features", "SaaS"),
(58, "Enhance AI responses", "SaaS"),
(59, "Add user accounts + DB schema", "SaaS"),
(60, "Authentication + login system", "SaaS"),
(61, "Add usage tracking (tokens)", "SaaS"),
(62, "Logging + monitoring", "SaaS"),
(63, "Optimize prompts (reduce cost)", "SaaS"),
(64, "Improve cost efficiency", "SaaS"),
(65, "Add caching layer", "SaaS"),
(66, "Optimize performance", "SaaS"),
(67, "Docker setup", "SaaS"),
(68, "Deploy SaaS app", "SaaS"),
(69, "Add analytics dashboard", "SaaS"),
(70, "Improve analytics UI", "SaaS"),
(71, "UI polish + animations", "SaaS"),
(72, "Bug fixing", "SaaS"),
(73, "Performance improvements", "SaaS"),
(74, "Final polish", "SaaS"),
(75, "Production-ready build", "SaaS"),

# 💼 DAYS 76–90 (Job Hunt)
(76, "Apply to 10–20 jobs", "Job Hunt"),
(77, "DM recruiters + founders", "Job Hunt"),
(78, "Continue applications", "Job Hunt"),
(79, "Prepare interview answers", "Job Hunt"),
(80, "Revise projects + resume", "Job Hunt"),
(81, "Mock interviews", "Job Hunt"),
(82, "Apply + network", "Job Hunt"),
(83, "Improve weak areas", "Job Hunt"),
(84, "Follow up with recruiters", "Job Hunt"),
(85, "Interview practice", "Job Hunt"),
(86, "More applications", "Job Hunt"),
(87, "Refine portfolio", "Job Hunt"),
(88, "Final interview prep", "Job Hunt"),
(89, "Offer negotiation prep", "Job Hunt"),
(90, "Review progress + next steps", "Job Hunt"),
]

# Insert into DB
for day_number, task, phase in days_data:
    db.add(Day(day_number=day_number, task=task, phase=phase))

db.commit()
db.close()

print("✅ Seeded 90-day roadmap successfully!")