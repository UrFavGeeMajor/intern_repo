# Study Notes: Logical & Physical Channels in DVB-S2X and DVB-RCS2

* **Author:** Petrajoy Davidson  
* **Date:** 2025-08-13 – 2025-08-13  
* **Goal:** Understand the distinction between logical and physical channels in DVB systems, and how they relate to the system architecture & L1 framing.  
* **Slides:** 37–38  

---

## 1. Core Principle Discovered: Separation Between “What” and “How” Data is Sent

The key insight from these slides is that **logical channels describe the type of information being carried**, while **physical channels describe how that information is transmitted over the satellite link**.  
This separation is critical because the same logical channel can be mapped to different physical resources depending on network conditions, modulation schemes, or service requirements.

---

## 2. System Analysis: Following the Data Mapping

### 2.1. Slide 37 — Intro to Logical & Physical Channels
<img width="1824" height="714" alt="image" src="https://github.com/user-attachments/assets/7b71c30f-6fb9-47a9-a23e-9c5837cf9132" />

**Function:**  
Introduce the concept of separating the "data meaning" layer from the "physical transmission" layer.

**Visual Breakdown:**  
- **Top layer:** Logical Channels — functional data flows (user traffic, signaling, control info).  
- **Bottom layer:** Physical Channels — actual time slots, frequencies, and modulation parameters used for transmission.

**Technical Essence:**  
- Logical channels are **abstract**; they exist in the MAC layer and above.  
- Physical channels are **concrete**; they exist in the PHY layer.  
- The mapping between them is dynamic, depending on system scheduling, ACM, and link conditions.

**Analogy:**  
Logical channels = **postal letters** (content type: invoice, postcard, invitation).  
Physical channels = **delivery trucks** (size, route, speed).  
The same type of letter can go in different trucks depending on capacity and priority.

---

### 2.2. Slide 38 — What Are Logical Channels
<img width="1228" height="1125" alt="image" src="https://github.com/user-attachments/assets/8d2e5968-c352-4ce7-a49b-08e8531a7193" />

**Function:**  
Define the different logical channel types in the DVB context.

**Visual Breakdown:**  
- **User Traffic Channels:** GSE or MPEG-TS carrying IP/data payloads for end users.  
- **Control Channels:** Network management instructions from hub to terminals (e.g., return link slot assignments).  
- **Signaling Channels:** Essential L1 info like PLS codes, MODCOD, and timing.

**Technical Essence:**  
- Logical channels are **service-oriented**: they exist to fulfill specific communication purposes.  
- They are **multiplexed together** before being mapped to physical layer frames.  
- DVB systems treat them as independent flows so that control & signaling can be maintained even when user data is low or absent.

**Key Takeaway:**  
Logical channels don't care about frequency, symbol rate, or burst timing — only about **what** is being communicated. The MAC scheduler later decides the **how**.

---

## 2.3. Slide 39 — What Are Physical Channels
<img width="594" height="1125" alt="image" src="https://github.com/user-attachments/assets/549c7fcf-0889-4c74-9bd0-fee72a20d99f" />

**Function:**  
Explain the concept of physical channels as the actual transmission resources that carry logical channels over the air.

**Visual Breakdown:**  
- **Frequency Domain:** Different carriers or subcarriers assigned for transmission.  
- **Time Domain:** Slots, bursts, or frames assigned to users.  
- **Code Domain (if applicable):** Spreading codes (not common in DVB-S2X, but relevant in multi-access systems).

**Technical Essence:**  
- Physical channels are defined in the PHY layer — they are measurable in hertz, symbols, and seconds.  
- DVB-S2X forward link: Physical channel = continuous carrier stream with a defined MODCOD.  
- DVB-RCS2 return link: Physical channel = MF-TDMA burst slot in a shared carrier.

**Key Note:**  
Mapping logical channels to physical channels involves **MAC scheduling**: deciding which data goes into which burst, carrier, and time slot.

---

## 2.4. Slide 40 — Logical Channels in DVB-S2X
<img width="1320" height="756" alt="image" src="https://github.com/user-attachments/assets/34290b92-9133-4f2f-ab70-8f4a6b72ca08" />

**Function:**  
Detail the logical channel structure used in the DVB-S2X forward link.

**Visual Breakdown:**  
- **User Traffic Logical Channels:**  
  - GSE streams encapsulating IP packets.  
  - MPEG-TS packets for broadcast services.  
- **Control & Signaling Logical Channels:**  
  - L1 Signaling (PLS codes, superframe info).  
  - ACM control commands from hub to terminal.  
  - Network management messages.

**Technical Essence:**  
- Logical channels are **multiplexed** into BBFRAMEs at the gateway.  
- The gateway prioritizes control/signal channels to ensure continuous service.  
- ACM (Adaptive Coding and Modulation) decisions happen before mapping logical channels to physical resources.

**Example:**  
During a rain fade, user data channels may be downshifted to a lower MODCOD, but control signaling channels still get sent at robust settings.

---

## 2.5. Slide 41 — Physical Channels in DVB-S2X
<img width="787" height="810" alt="image" src="https://github.com/user-attachments/assets/caed0571-24dd-4ced-8b7f-a50fdabb0557" />

**Function:**  
Show how logical channels are mapped onto DVB-S2X’s physical layer resources.

**Visual Breakdown:**  
- **Forward Link:**  
  - Continuous carrier stream at a fixed symbol rate.  
  - Time segmentation into PLFRAMEs.  
  - Each PLFRAME contains a mix of user traffic & signaling.

**Technical Essence:**  
- PLFRAME is the core physical transmission unit.  
- PLS Header indicates MODCOD, frame type, and pilot configuration.  
- Logical channels are packed into BBFRAMEs → mapped to PLFRAMEs → sent over the forward link carrier.

**Important Insight:**  
Unlike the return link, the forward link is **continuous** — no idle slots. All physical resources are constantly in use.

---

## 2.6. Slide 42 — Logical Channels in DVB-RCS2
<img width="1698" height="812" alt="image" src="https://github.com/user-attachments/assets/037fbc19-f8c8-4466-a261-430febe2d244" />

**Function:**  
Define the logical channel types for the DVB-RCS2 return link.

**Visual Breakdown:**  
- **User Traffic Logical Channels:**  
  - IP packet streams from user terminals.  
- **Control Logical Channels:**  
  - Return channel requests (RCST → NCC).  
  - Terminal configuration updates.  
- **Signaling Logical Channels:**  
  - Timing & frequency correction feedback.  
  - Link adaptation commands.

**Technical Essence:**  
- In the return link, logical channels must be **synchronized** with the NCC’s TDMA schedule.  
- Control and signaling channels are essential to coordinate burst timing and avoid collisions.  
- These logical channels are **short-lived** bursts, unlike the continuous forward link channels.

**Key Takeaway:**  
In DVB-RCS2, the logical channels are more dynamic — they appear/disappear based on traffic demand and NCC scheduling decisions.

---

## 2.7. Slide 43 — Physical Channels in DVB-RCS2
<img width="1008" height="469" alt="image" src="https://github.com/user-attachments/assets/bceb289c-7d7b-4be8-ae65-5a197ac99b0c" />

**Function:**  
Describe the physical resources that carry the DVB-RCS2 return link.

**Visual Breakdown:**  
- **MF-TDMA Carrier:** Shared by many RCSTs.  
- **Time Slots:** Divided within the carrier into bursts.  
- **Burst Types:**  
  - User data bursts.  
  - Control signaling bursts.  
  - Synchronization bursts.

**Technical Essence:**  
- Each RCST is assigned one or more **time slots** by the NCC.  
- Slots are defined in both **time** and **frequency**.  
- Modulation & coding for bursts can vary per user and per slot based on link conditions.  
- Burst framing contains **guard times** to account for satellite round-trip delay and prevent overlap.

**Key Insight:**  
Physical channels in RCS2 are not continuous — they are **reserved and intermittent** according to demand and scheduling.

---

## 2.8. Slide 44 — Channel Mapping: Gateway → RCST
<img width="963" height="1125" alt="image" src="https://github.com/user-attachments/assets/3fe544cb-4a34-4e54-8dd6-2114e22f23c4" />

**Function:**  
Show how the forward link channels are organized and mapped from the gateway to the user terminal.

**Visual Breakdown:**  
- Logical Channels: User traffic, control, and signaling.  
- Mapping Process:  
  1. Multiplex logical channels into BBFRAMEs.  
  2. Encode & modulate into PLFRAMEs.  
  3. Transmit over continuous forward link carrier.

**Technical Essence:**  
- All RCSTs receive the **same forward carrier**, but each extracts only the data addressed to it.  
- Control signaling (e.g., burst assignments, timing corrections) is sent alongside user traffic in the same carrier.  
- Priority is given to control channels to ensure reliable terminal operation.

**Example:**  
A single PLFRAME might carry:  
- IP video data for RCST A.  
- Web traffic for RCST B.  
- NCC schedule update for all RCSTs.

---

## 2.9. Slide 45 — Channel Mapping: RCST → Gateway
<img width="965" height="1049" alt="image" src="https://github.com/user-attachments/assets/bd1a2e67-620f-452a-8f60-ed3988154143" />

**Function:**  
Explain how channels are mapped in the return direction from the RCST to the gateway.

**Visual Breakdown:**  
- Logical Channels: User data, return channel requests, status reports.  
- Mapping Process:  
  1. Logical channels packetized into bursts.  
  2. Assigned to time slots by NCC.  
  3. Modulated and sent during assigned slot.

**Technical Essence:**  
- Only one RCST transmits in a slot to avoid collisions.  
- Slots can be allocated dynamically depending on demand.  
- Control bursts (e.g., logon requests) often use more robust MODCODs than user data bursts.

**Key Point:**  
Return link efficiency depends heavily on NCC scheduling — underutilized slots waste capacity, over-allocations cause delays.

---

## 2.10. Slide 46 — Recap: Channel Abstraction vs Reality
<img width="1237" height="871" alt="image" src="https://github.com/user-attachments/assets/904794f2-19a8-49b1-9d7c-e4cfbe18bb38" />

**Function:**  
Summarize the conceptual difference between logical and physical channels, and how they interact in practice.

**Conceptual Recap:**  
- **Logical Channels:** Defined in the MAC layer. Represent flows of specific types of data (user, control, signaling).  
- **Physical Channels:** Defined in the PHY layer. Represent actual transmission resources (carriers, bursts, slots).

**Reality Check:**  
- Logical channels are **not physically separate** — they are **multiplexed** over the same physical resources.  
- In the forward link, all logical channels share the same continuous carrier.  
- In the return link, logical channels are spread across intermittent time slots.

**Key Takeaways:**  
1. Logical channels = "What data is being sent."  
2. Physical channels = "Where, when, and how it is sent."  
3. DVB-S2X → Continuous carrier with multiplexing.  
4. DVB-RCS2 → Scheduled bursts in MF-TDMA grid.

**Study Insight:**  
Understanding the mapping between logical and physical channels is essential before integrating NTN NR, because NR also separates logical and physical layers in its design — making alignment much easier.
