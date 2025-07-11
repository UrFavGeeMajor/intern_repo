# Study Notes: DVB-RCS2 (ETSI EN 301 545-2) 🛰️

This document provides a summary of the key aspects of the **DVB-RCS2 (Second Generation DVB Interactive Satellite System)** standard, based on the official ETSI specification `EN 301 545-2 V1.2.1`. It defines the lower layers for the return link (uplink), designed to complement a DVB-S2/S2X forward link for interactive services.

---

##  Core Objectives and Applications

The primary objective of `DVB-RCS2` is to provide a flexible and highly efficient return channel for a large number of user terminals. It is designed to support a wide range of interactive applications by allowing its waveform, Forward Error Correction (FEC), and burst characteristics to be configured and adapted for different scenarios, from consumer broadband to professional data services.

---

##  System Architecture and Enhancements

`DVB-RCS2` operates in a **transparent star satellite network** topology. It introduces significant enhancements over the first-generation standard to improve efficiency and adaptability.

###  System Model

* **RCST (Return Channel Satellite Terminal):** The user terminal that transmits data on the uplink.
* **Gateway:** The central ground station that receives signals from all RCSTs.
* **NCC (Network Control Centre):** Located at the Gateway, this entity manages the network, controls terminal access, and allocates transmission resources.

###  Key Enhancements

* **MF-TDMA (Multi-Frequency Time Division Multiple Access):** This is the core access scheme. The return link bandwidth is divided into multiple carrier frequencies, and each frequency is time-sliced to be shared by multiple users transmitting in bursts.
* **Advanced Modulation & FEC:** Adds support for more spectrally efficient modulation schemes like **8PSK** and **16QAM**, as well as robust **Continuous Phase Modulation (CPM)**. FEC is enhanced with a powerful **16-state Turbo Code**.
* **Return Link Encapsulation (RLE):** A major improvement for handling IP packets. RLE allows user data to be fragmented "just-in-time" to perfectly fit into the variably-sized transmission burst payloads, significantly reducing overhead compared to older fixed-size methods.
* **Per-Timeslot ACM:** The system supports using different modulation and coding schemes for each individual timeslot, allowing for very granular and responsive link adaptation for each user terminal.

---

##  Frame Structure & Key Components

The uplink is organized in a clear hierarchy, from the overall timing structure down to the individual data bursts sent by the terminals.

###  Return Link Time Structure

The MF-TDMA resources are organized as follows:

1.  **Superframe:** The largest time division, defined by the `Superframe Composition Table (SCT)`.
2.  **Frame:** Each superframe is divided into one or more frames. The `Frame Composition Table (FCT2)` defines the timeslot organization for different frame types.
3.  **Timeslot:** The fundamental unit of transmission opportunity (a specific time on a specific frequency) that the NCC allocates to an RCST.

###  Encapsulation and PDU Hierarchy

The **Return Link Encapsulation (RLE)** protocol prepares user data for transmission through a multi-stage process:

1.  A user's **SDU (Service Data Unit)** is first wrapped into an **ALPDU (Addressed Link PDU)**.
2.  The ALPDU is then segmented into one or more **PPDUs (Payload-adapted PDUs)** to fit into the allocated physical layer slots.
3.  Finally, one or more PPDUs are assembled into a single **FPDU (Frame PDU)**, which becomes the payload of a transmission burst.

###  Transmission Burst Components

The final physical transmission sent from the RCST is a burst containing:

* **Preamble/Unique Word (UW):** A known sequence at the start of the burst for receiver synchronization.
* **Payload:** The FPDU containing the user data, protected by robust Forward Error Correction (FEC).
* **Pilots:** Optional known symbols inserted within the payload to aid in channel tracking.
* **Post-amble:** An optional sequence at the end of the burst.
