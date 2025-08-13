# Study Notes: Layer 1 (L1) Framing in DVB Systems

* **Author:** Petrajoy Davidson  
* **Date:** 2025-08-13 – 2025-08-14  
* **Goal:** Understand and document the complete Layer 1 (L1) framing process in DVB-S2X and DVB-RCS2, linking it to the broader question: *"How can we implement NTN NR on top of DVB L1?"*  
* **Slides:** 24–35  

---

## 1. Core Principle Discovered: The “Container” Logic of DVB L1

L1 framing in DVB systems acts as the **physical-level container** that all logical data flows, control signals, and timing structures must fit into before they can be transmitted.  
Although the forward (S2X) and return (RCS2) links share the same *conceptual* job — structuring bits into frames — their framing architectures are **very different** because of the **traffic pattern asymmetry** and **medium access methods**.

- **Forward Link (DVB-S2X):** Continuous stream → Big, fixed-size containers (BBFRAME → PLFRAME → Superframe) → Maximize efficiency.  
- **Return Link (DVB-RCS2):** Burst-based MF-TDMA slots → Small, time-bound containers (Bursts → Slots → Frames) → Maximize coordination.

---

## 2. Detailed Slide-by-Slide Study Notes

---

### Intro to L1 Framing (DVB-S2X & RCS2)**
<img width="648" height="753" alt="image" src="https://github.com/user-attachments/assets/641c7fa1-c2cb-4a58-8410-cad2561919fc" />

**Visual Analysis:**  
- Left side shows **DVB-S2X forward link** with a continuous stream of PLFRAMEs, each with PLS headers and pilots, organized inside Superframes.
- Right side shows **DVB-RCS2 return link** with bursts arranged in an MF-TDMA time-frequency grid, separated by guard intervals.

**Technical Essence:**  
- **Purpose:** L1 framing ensures that the modulator and demodulator can stay synchronized, know frame boundaries, and recover data correctly.
- **DVB-S2X Forward Link:**
  - Continuous carrier.
  - Strict symbol and frame alignment.
  - Efficiency-optimized: minimal unused space, large frames to reduce header overhead.
- **DVB-RCS2 Return Link:**
  - Burst transmissions (no constant carrier from each terminal).
  - Requires precise slot timing to prevent collisions.
  - NCC assigns frequency + time slot to each terminal.

**Key Takeaway:**  
Forward link framing is **broadcast and continuous**. Return link framing is **scheduled and discrete**.

---

### Baseband Frame (BBFRAME) Structure**
<img width="1206" height="184" alt="image" src="https://github.com/user-attachments/assets/23688c45-e21e-47ac-a0d6-fca6c30a936e" />

**Visual Analysis:**  
- Frame divided into:
  1. **BBHEADER** — contains metadata.
  2. **Payload Area** — GSE or MPEG-TS packets.

**Technical Essence:**
- **BBHEADER:** Contains metadata like frame length, stream type, and MODCOD indicator.  
- **Payload:** GSE packets or MPEG-TS packets.  
- BBFRAME size is constant for a given MODCOD/FEC rate.  
- Acts as the bridge between upper-layer encapsulation and FEC processing.
- **BBHEADER Fields:**
  - Stream type (GSE, TS, etc.).
  - Payload length.
  - MODCOD ID.
  - Header CRC.
- **Payload Area:**
  - Holds encapsulated data.
  - May contain padding to match fixed frame size.
- **Purpose of BBFRAME:**
  - Creates a fixed, predictable input size for the FEC stage.
  - Decouples encapsulation from physical layer processing.

**Example Flow:**  
IP packets → GSE encapsulation → BBFRAME (BBHEADER + Payload) → FEC encoding.
  
---

### Forward Error Correction: LDPC + BCH**
<img width="1400" height="210" alt="image" src="https://github.com/user-attachments/assets/06fd7a0a-fdd8-4ccf-817e-2a61ed02ad62" />

**Visual Analysis:**  
- BBFRAME enters LDPC encoder → BCH encoder → produces FECFRAME → goes to modulation.
- Two frame sizes: Normal (64,800 bits) and Short (16,200 bits).

**Technical Essence:**  
- **LDPC:** Strong block code for correcting many random bit errors (main workhorse).  
- **BCH:** Shorter block code added after LDPC to clean up residual errors.  
- Resulting **FECFRAME** is larger than BBFRAME due to parity bits.  
- DVB-S2X supports **normal** and **short** FECFRAME lengths depending on service needs.
- **LDPC:**
  - Powerful block code using sparse parity-check matrices.
  - Corrects the majority of transmission errors.
  - Operates on the full frame payload.
- **BCH:**
  - Applied after LDPC to fix any residual bit errors.
  - Essential for achieving ultra-low BER targets.
- **Output:** FECFRAME is larger than BBFRAME due to parity bits.
- **Why Both Codes?**
  - LDPC provides high correction capability but may leave small errors.
  - BCH guarantees clean frames for both data and control signals.

**Extra Insight:**  
This two-stage FEC lets DVB operate reliably even in **low SNR or harsh conditions** (e.g., rain fade, Ka-band, NTN high latency).

---

### PLFRAME Composition & PLS Header**
<img width="2000" height="312" alt="image" src="https://github.com/user-attachments/assets/58aab50b-f9f8-41c2-bf2a-426f2d314354" />

**Visual Analysis:**  
- Frame layout: **PLS Header → Pilot Blocks → Data Symbols**.
- PLS (Physical Layer Signaling) header is short but critical — tells the receiver **how to decode** the rest of the frame.
- Pilots are scattered in predictable positions.

**Technical Essence:**  
- **PLS Header:** Tells the receiver how to decode this frame (MODCOD, FEC type, pilot pattern).  
- **Data field:** Contains modulated symbols for payload.  
- **Pilot blocks:** Known reference symbols for synchronization & channel estimation.  
- PLFRAME = FECFRAME + pilot insertion + PLS header.
- **PLS Header:**
  - Contains MODCOD info (modulation type + FEC rate).
  - Indicates frame length (Normal or Short).
  - Includes scrambling sequence ID (for receiver sync).
  - Encoded with a robust BPSK scheme to survive very low SNR.
- **Pilots:**
  - Known symbol patterns inserted periodically.
  - Used for:
    - Coarse & fine frequency synchronization.
    - Phase tracking.
    - Doppler estimation (important for NTN).
- **Payload Symbols:**
  - Carry the modulated FECFRAME bits.
  - Interleaved to spread out errors.


---

### MODCOD Mapping & ACM in DVB-S2X**
<img width="867" height="488" alt="image" src="https://github.com/user-attachments/assets/d286e197-b9b0-4946-8dab-25d05a8a5e21" />

**Visual Analysis:**  
- Table mapping MODCOD IDs to Modulation Type (QPSK, 8PSK, 16APSK, 32APSK) and FEC rates.
- ACM (Adaptive Coding and Modulation) loop: **Terminal measures SNR → reports to gateway → gateway adjusts MODCOD**.

**Technical Essence:**  
- **MODCOD:** Combination of modulation order (QPSK, 8PSK, 16APSK, etc.) and FEC rate.  
- **ACM (Adaptive Coding & Modulation):** Changes MODCOD in real-time per terminal link conditions.  
- MODCOD choice impacts BBFRAME size and error resilience.  
- ACM signaling is carried in the **PLS header**.
- **MODCOD:**
  - Each MODCOD is a predefined combination of modulation scheme + FEC rate.
  - Higher MODCOD = more bits/symbol, but needs higher SNR.
- **ACM:**
  - Dynamically selects MODCOD per terminal or per frame.
  - In forward link: ACM adapts to changing weather, link margin.
- **NTN Implication:**
  - Long RTT makes ACM trickier — SNR can change before the new MODCOD is applied.
  - Might need predictive ACM or margin buffers.

**Example:**  
- Good link: 32APSK 9/10 → high throughput.  
- Rain fade: Switch to QPSK 1/3 → survives but slower.  

---

### Superframe Structure**
<img width="914" height="651" alt="image" src="https://github.com/user-attachments/assets/21a0af2b-19eb-411f-b673-0619a89dd209" />

**Visual Analysis:**  
- Continuous superframe: several PLFRAMEs in sequence.
- Superframe header at start → contains timing and frame mapping info.
- Alignment across multiple carriers for multistream and beam-hopping.

**Technical Essence:**  
- Superframe = Fixed-duration container for multiple PLFRAMEs.  
- Contains **superframe header**, **pilot/reference blocks** for beam hopping, and time markers.  
- In multi-beam systems, superframe alignment ensures time/frequency synchronization.
- **Purpose:**
  - Align all physical layer frames in time for:
    - Multi-beam coordination.
    - Beam-hopping schedules.
    - Multi-carrier systems.
- **Contents:**
  - Superframe Header: robust signaling about frame boundaries.
  - Filler/Pilots to maintain symbol alignment.
- **Why Matters for NTN:**
  - Satellite switching beams needs precise superframe alignment so terminals know **exactly when their frame starts**.

**Key Note:**  
Superframe is like the "calendar" of the forward link — without it, there’s no global timing reference.

---

### Return Link Burst Framing (MF-TDMA in DVB-RCS2)**
<img width="1062" height="555" alt="image" src="https://github.com/user-attachments/assets/f5c9a356-ec7e-459c-a13b-5428ed81ef34" />

**Visual Analysis:**  
- Burst frame structure: **Guard Time → Burst Preamble → Payload Symbols → Guard Time**.
- Bursts fit into TDMA slots across frequency and time.

**Technical Essence:**  
- Return link divided into **frames** of fixed time duration.  
- Each frame subdivided into **slots**; slots assigned to terminals by NCC.  
- **Burst:** Time-limited packet of modulated data from an RCST.  
- Burst framing includes preamble for sync, payload, and guard time.
- **MF-TDMA (Multi-Frequency TDMA):**
  - Many carriers (frequencies), each with time slots.
  - Terminals hop to their assigned frequency and transmit in their slot.
- **Burst Preamble:**
  - Known symbols for timing/frequency lock.
  - Compensates for satellite motion & Doppler.
- **Guard Times:**
  - Prevent bursts from overlapping due to timing errors or varying distances.
- **Payload:**
  - Encoded data, usually in short FEC frames.

---

### MF-TDMA Burst Grid in Return Link (DVB-RCS2)**
<img width="1031" height="485" alt="image" src="https://github.com/user-attachments/assets/347e16d8-50f3-4294-b331-86d96d976042" />

**Visual Analysis:**  
- Time on x-axis, frequency on y-axis → grid of burst slots.
- Each colored cell = a terminal’s transmission opportunity.
- Slots are dynamically allocated by NCC.

**Technical Essence:**  
- Multiple carriers (frequencies) each have their own time-slot grid.  
- Slots can be reused across carriers to maximize capacity.  
- Terminals must switch frequency & timing based on NCC assignment.
- **NCC Role:**
  - Assigns bursts based on demand and QoS priority.
  - Avoids collisions by controlling slot allocation.
- **Dynamic Slot Allocation:**
  - Higher demand terminals may get more slots.
  - Unused slots can be reassigned quickly.
- **Scalability:**
  - Multiple carriers × multiple slots per frame.
  - Thousands of users can share the link efficiently.

**Analogy:**  
Think of it like a **multi-lane highway toll booth**:  
- Lanes = frequencies.  
- Time slots = the toll booth letting one car pass at a time. 

---

### Slot Assignment Strategy in DVB-RCS2**
<img width="701" height="1125" alt="image" src="https://github.com/user-attachments/assets/86e0b1a4-dc74-4470-aef8-efbb2131c4fa" />

**Visual Analysis:**  
- Diagram shows NCC controlling slot allocation per RCST.  
- Multiple traffic classes mapped to slots — priority-based.  
- Dynamic reassignment when demand changes.

**Technical Essence:**  
- NCC allocates slots per terminal per frame.  
- Assignments adapt to traffic load, QoS requirements, and link quality.  
- Reduces wasted capacity compared to static allocation.
- **QoS-Based Allocation:**
  - Each slot is tagged with a service class (e.g., high-priority VoIP vs. best-effort browsing).
  - Real-time flows get guaranteed slots.
- **Dynamic Reallocation:**
  - NCC monitors terminal demand in real-time.
  - If a user is idle, their slots can be reassigned temporarily.
- **Reservation Methods:**
  1. **CRA** (Continuous Rate Assignment) — Fixed slots for predictable traffic.
  2. **VBDC** (Volume-Based Dynamic Capacity) — Assign slots based on queued data volume.
  3. **RBDC** (Rate-Based Dynamic Capacity) — Assign slots based on requested transmission rate.
  4. **ACM Integration** — Higher MODCOD can fit more bits into the same slot, reducing slot count needed.

---

### RCST Return Burst Timing**
<img width="1592" height="275" alt="image" src="https://github.com/user-attachments/assets/c387e15e-d305-439f-9d76-92b0d6409615" />

**Visual Analysis:**  
- Timeline showing guard times, burst transmission, and clock alignment signals.
- RCST’s clock synchronized to the NCC via timing beacons.

**Technical Essence:**  
- Terminals must pre-compensate timing to arrive exactly within assigned slot.  
- **Guard time** inserted to avoid overlap due to timing jitter or Doppler shifts.  
- NCC periodically sends timing corrections.
- **Two-Way Timing Alignment:**
  - Forward link carries timing reference.
  - RCST adjusts its clock to match NCC’s master time.
- **Propagation Delay Compensation:**
  - NCC calculates each terminal’s round-trip delay.
  - RCST pre-compensates its burst start time so it arrives exactly in its slot.
- **Guard Time Role:**
  - Absorbs small timing errors due to clock drift or orbital movement.
- **NTN Twist:**
  - LEO/MEO motion means delay changes over time → periodic re-calibration needed.

**Key Insight:**  
Return burst timing is like **precision choreography** — every RCST must dance in step with NCC’s master clock.

---

### RCS2 Modulation & Coding**
<img width="1312" height="589" alt="image" src="https://github.com/user-attachments/assets/bc215827-8a92-45d0-a6a1-97fb6065fc24" />

**Visual Analysis:**  
- Table mapping return link modulation types (QPSK, 8PSK, 16QAM) to FEC rates.
- Multiple MODCODs used depending on terminal conditions.

**Technical Essence:**  
- Modulation order depends on return link SNR.  
- FEC choices balance reliability vs throughput.  
- Lower MODCOD → higher robustness, used for weak links.
- **MODCOD Selection:**
  - Chosen per RCST or per burst.
  - Low SNR → robust coding (e.g., QPSK 1/3).  
  - High SNR → higher-order modulation (e.g., 16QAM 7/8).
- **Error Correction:**
  - LDPC + BCH for robustness.
  - Short FEC frames common in return link to reduce latency.
- **ACM in Return Link:**
  - More complex than forward link due to MF-TDMA structure — requires per-slot adjustment.
- **NTN Considerations:**
  - Doppler shift can distort constellation → adaptive equalization needed before demodulation.

**Example:**  
During rain fade, an RCST may drop from 8PSK 5/6 to QPSK 2/3 to maintain link reliability.

---

### Recap: End-to-End Framing**
<img width="1270" height="1125" alt="image" src="https://github.com/user-attachments/assets/3f667e25-d66e-4b31-97f9-0b78e4b54593" />

**Visual Analysis:**  
- Combined diagram of forward and return link framing:
  - Forward: **IP → GSE → BBFRAME → FECFRAME → PLFRAME → Superframe**.
  - Return: **IP → MAC → Burst Frame → TDMA Slot → Carrier Grid**.
  - - Forward link: Continuous superframes with PLFRAMEs.  
  - Return link: Discrete bursts in MF-TDMA grids.  
  - L1 framing aligns **logical channel mapping** with physical transmission timing.

**Core Takeaways:**
1. **Forward Link (DVB-S2X):**
   - Designed for continuous, high-throughput broadcasting.
   - Relies on superframes for timing & alignment.
   - ACM adjusts MODCOD per terminal for efficiency.

2. **Return Link (DVB-RCS2):**
   - Designed for many users sharing the uplink.
   - Uses MF-TDMA with dynamic slot assignment.
   - Requires precise burst timing and guard times.

3. **Common to Both:**
   - Layer 1 framing is the bridge between digital packets and satellite RF transmission.
   - Synchronization (PLS headers, pilots, superframes) is key for decoding.  


---

## 3. Key Takeaways & L1 Framing Recap

1. **Framing is the Physical “Box”:** Both S2X and RCS2 rely on L1 frames to package data for the satellite channel, but the packaging logic differs.
2. **Forward = Efficiency, Return = Coordination:**  
   - Forward link optimizes for throughput and continuous flow.  
   - Return link optimizes for collision-free shared access.  
3. **Timing is Central:** Superframe boundaries in S2X and MF-TDMA slot boundaries in RCS2 both enforce global time alignment.  
4. **MODCOD Flexibility:** Both links adapt their MODCODs to link conditions, but S2X often uses ACM for individual users, while RCS2 applies it per burst.  
5. **Guard and Sync:** Physical layer preambles, pilots, and guard intervals ensure that L1 frames can be received reliably despite satellite impairments.

---

## 4. Next Steps

Move on to **Logical & Physical Channels** section:
- Map which data flows (user, control, signaling) go into which logical channels.
- Understand how logical channels are multiplexed into physical carriers, slots, and frames.
- Prepare to relate this to NTN NR channelization.
