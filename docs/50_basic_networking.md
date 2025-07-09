# Module 5: Communication Principles

## 5.1 Communication Protocols

### 5.1.1 Communication Protocols
- Protocols are **sets of rules** that determine how data is transmitted.
- Ensure devices can communicate reliably, even if built by different manufacturers.

### 5.1.2 Why Protocols Matter
- Enable **interoperability** across devices/networks.
- Without protocols: inconsistent communication, data loss, or complete failure.
- Examples: HTTP, TCP, IP, FTP, DNS.

---

## 5.2 Communication Standards

### 5.2.1 The Internet and Standards
- Internet relies on **open standards** to ensure global compatibility.
- Standards make it possible for anyone to build hardware/software that connects seamlessly.

### 5.2.2 Network Standards Organizations
- **IETF (Internet Engineering Task Force)**: Develops internet protocols like TCP/IP.
- **IEEE (Institute of Electrical and Electronics Engineers)**: Creates LAN/Wi-Fi standards (e.g., 802.11).
- **ISO (International Organization for Standardization)**: Maintains OSI Model and more.
- **ITU (International Telecommunication Union)**: Global telecom standards, includes satellite comms.

---

## 5.3 Network Communication Models

### 5.3.1 Network Protocols
- Work together in **layers** to ensure end-to-end delivery.
- Each layer has specific roles (e.g., addressing, routing, error-checking).

### 5.3.2 The Protocol Stack
- A **stack** is a layered model of how network protocols interact.
- Common stacks:
  - **TCP/IP** (practical model)
  - **OSI** (conceptual reference model)

### 5.3.3 The TCP/IP Model
- 4 Layers:
  1. **Application**: HTTP, DNS, SMTP
  2. **Transport**: TCP, UDP
  3. **Internet**: IP, ICMP
  4. **Network Access**: Ethernet, Wi-Fi
- Real-world model used for the internet.

### 5.3.4 The OSI Reference Model
- 7 Layers:
  1. Application  
  2. Presentation  
  3. Session  
  4. Transport  
  5. Network  
  6. Data Link  
  7. Physical  
- Used as a **teaching/diagnostic tool**.

### 5.3.5 OSI Model and TCP/IP Model Comparison
| Layer | OSI Model | TCP/IP Model |
|-------|-----------|----------------|
| 7     | Application | Application |
| 6     | Presentation | — |
| 5     | Session | — |
| 4     | Transport | Transport |
| 3     | Network | Internet |
| 2     | Data Link | Network Access |
| 1     | Physical | Network Access |

- TCP/IP combines OSI layers 5–7 into a single **Application layer**.
- OSI is more granular; TCP/IP is simpler and used in practice.

---
