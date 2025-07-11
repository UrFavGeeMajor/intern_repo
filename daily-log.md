# 📚 Internship Documentation
---

## 🏁 Milestones

### 1. Getting Started with Telecom Networks
- [x] [1.1 Introduction to Networking](docs/networking.md#11-introduction-to-networking)

### 2. Deep Dive into O-RAN Components
- [x] [2.1 Service Management and Orchestration (SMO)](docs/oran/smo.md#21-service-management-and-orchestration)
- [ ] [2.2 RIC and E2 Nodes](docs/oran/ric.md#22-ric-and-e2-nodes)
- [ ] 2.3 Real-world Implementation Examples

### 3. Satellite-Based Digital Twin in Marine Science
- [ ] [3.1 Literature Review and Background Study](docs/sat/filename)
- [ ] [3.2 Satellite Data Exploration](docs/sat/filename)
- [ ] [3.3 Early Conceptual Model](docs/sat/filename)
- [ ] [3.4 Integration with O-RAN and 5G NTN](docs/sat/filename)

### 4. Study DVB-S2X and DVB-RCS2
Specs To Read:
- [x] ETSI EN 302 307-2 (DVB-S2X)
- [x] ETSI EN 301 545-2 (DVB-RCS2)
System Architecture
- [x] Diagram: DVB-S2X (Downlink)
    - [x] Feeder Terminal (FT)
    - [x] Satellite Payload
    - [x] User Terminal (UT)
- [x] Diagram: DVB-RCS2 (Uplink)
    - [x] UT → Satellite → FT (Return Link)
Frame Structure
- [ ] DVB-S2X:
    - [ ] Identify Data, Control, Management channels
    - [ ] Superframes and slicing
- [ ] DVB-RCS2:
    - [ ] Return Link Frame (RLF) structure
    - [ ] Signaling formats
Modulation & Protocol Comparison
- [ ] Table: QPSK, 8PSK, 16APSK, 32APSK
- [ ] FEC schemes used
- [ ] ACM mechanisms
- [ ] DL vs UL protocol stack

### 5. Study Resource Management Papers For DVB
- [x] System architecture & operational flow
- [ ] QoS requirement breakdown:
    - [ ] Bandwidth per service type (VoIP, video, best-effort)
- [ ] Beam hopping algorithm:
    - [ ] Beam count (4–16), traffic adaptation
    - [ ] Frequency reuse handling
- [ ] Routing algorithm:
    - [ ] MPLS-based LSP creation
    - [ ] Label distribution techniques (e.g., RSVP-TE)
- [ ] Service classes handled:
    - [ ] EF (Expedited Forwarding)
    - [ ] AF (Assured Forwarding)
    - [ ] BE (Best Effort)
Suggested Papers to Start With
- [ ] DVB-RCS2 Scheduling and Resource Management (IEEE)
- [ ] Beam Hopping Optimization in GEO VHTS (IEEE)
- [ ] QoS Routing in Satellite IP/MPLS Networks (Elsevier)

### 6. Evaluate Algorithm Performance
Tool Setup
- [ ] Install ns-3 + NTN module
- [ ] Setup Xeoverse 
Simulations to Run
- [ ] Beam hopping with 16 beams (non-uniform demand)
    - [ ] Metrics: throughput, fairness, delay
- [ ] Routing with MPLS under service classes
    - [ ] EF, AF, BE flows
    - [ ] Topology: 5–10 nodes (satellite routers)
Record Performance Stats
- [ ] Packet Delivery Ratio
- [ ] Latency / Jitter
- [ ] Throughput
- [ ] Beam switching delays
- [ ] QoS satisfaction rates

## 📆 Daily Logs

### 2025-07-07

**🎯 Short-term Goal:**  
1. [Milestone 1: Getting Started with Telecom Networks](docs/networking.md)

**📝 Daily Logs:**  
- `08:30–10:00`: [1.1 Intro to Networking](docs/networking.md#11-introduction-to-networking)
- `10:15–11:30`: Making A Trello Card and GitHub Repository
- `13:00–15:00`: Completed [Module 1 : Communication in a Connected World](docs/networking.md#11-introduction-to-networking)

---

### 2025-07-08

**🎯 Short-term Goal:**  
1. [Milestone 1: Getting Started with Telecom Networks](docs/networking.md)

**📝 Daily Logs:**  
- `08:00–14:00`: Passport administration and document preparation for NTUST internship (non-technical task)  
- `14:00–15:30`: Completed [Module 2 : Network Components, Types, and Connections](docs/networking.md#11-introduction-to-networking)

---

- ### 2025-07-09

**🎯 Short-term Goal:**  
1. [Milestone 1: Getting Started with Telecom Networks](docs/networking.md)

**📝 Daily Logs:**  
- `08:30–10:00`: Reviewed and completed [Module 3: Wireless and Mobile Networks](docs/networking.md#11-introduction-to-networking)
- `10:15–12:00`: Completed [Module 4: Build a Home Network](docs/networking.md#11-introduction-to-networking) and Checkpoint Exam  
- `13:00–14:00`: Studied [Module 5: Communication Principles](docs/networking.md#11-introduction-to-networking)
- `14:15–15:30`: Continued [Module 6: Network Media](docs/networking.md#11-introduction-to-networking)

---

- ### 2025-07-10

**🎯 Short-term Goal:**  
1. [Milestone 1: Getting Started with Telecom Networks](docs/networking.md)

**📝 Daily Logs:**  
- `08:30–10:00`: Reviewed and completed [Module 6: Wireless and Mobile Networks](docs/networking.md#11-introduction-to-networking)
- `10:15–12:00`: Completed [Module 7: Build a Home Network](docs/networking.md#11-introduction-to-networking)
- `13:00–14:00`: Studied [Module 8: Communication Principles](docs/networking.md#11-introduction-to-networking)
- `14:15–15:30`: Continued [Module 9: Network Media](docs/networking.md#11-introduction-to-networking)

---

- ### 2025-07-11

**🎯 Short-term Goal:**  
[Milestone 4: Study DVB-S2X and DVB-RCS2]
Short-term Goals:
- Skim official DVB-S2X and DVB-RCS2 specifications (ETSI)
- Identify core architecture components: UT, FT, Satellite
- Sketch draft system diagram

**📝 Daily Logs:**  
- `9:00–12:00`: Read basic S2X/RCS2 descriptions, Jotted down key differences (DL vs UL)
- `13:00–17:00`: Found ETSI TS 102 606 (S2X) and TS 101 545-2 (RCS2), Started rough block diagram in notebook
