# Skim Paper/Journal: Part 2. 🔍
Journal name = Innovative DAMA algorithm for multimedia DVB-RCS system by Carlos de la Cuesta, et al. Published in EURASIP Journal on Wireless Communications and Networking, 2013.
What we discussing :
- Focused on identifying traffic models:
  - CRA (Constant Rate)
  - RBDC (Rate-Based)
  - RA (Random Access)
- Started comparative matrix (traffic type × allocation method)
- Extracted QoS approaches
  - DSCV-Based Classification (DiffServ)
  - Use of priority queues

## Paper's Definition
- **CRA (Continuous Rate Assignment)**: This is a rate capacity that "shall be provided in full while required". Think of it as opening a dedicated, continuous pipe for a service.
- **RBDC (Rate-Based Dynamic Capacity)**: This is a rate capacity that is requested dynamically by the user terminal (RCST). The paper adds that these requests are "absolute,"  meaning each new request replaces the previous one.
- **VBDC (Volume-Based Dynamic Capacity)**: This is a volume capacity requested dynamically by the RCST. Unlike RBDC, these requests are "cumulative,"  meaning the NCC adds the new request to any previously unfulfilled volume.
- **RA (Random Access)**: The paper mentions that the new DVB-RCS2 standard allows for random access to optimize resource usage. However, the paper's focus is on the DAMA mechanisms (CRA, RBDC, VBDC) which involve explicit requests.

## Comparative Matrix (Traaffic Type x Allocation Method
| Request Method | Definition                                                                 | Best For (Application Type)                                                         | Key Characteristic / Finding from Paper                                                                                                                                                   |
|----------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CRA**        | A fixed, continuous data rate is allocated for the session’s duration.     | - High-quality, constant-bitrate services (e.g., VoIP, stable video stream)         | The DAMA controller checks if it can assign the full CRA rate **before** accepting a terminal’s logon request, ensuring guaranteed bandwidth.                                              |
| **RBDC**       | The terminal dynamically requests a specific **data rate**.                | - Real-time variable bitrate services (e.g., videoconferencing)                     | Has better request resolution (as low as 2 kbps), which reduces over-requesting for rate-adaptive applications. However, it performs poorly for bursty, short-lived traffic like web Browse. |
| **VBDC**       | The terminal dynamically requests a specific **volume** of data to send.   | - Bursty, transactional traffic (e.g., web browsing, email, file downloads)         | Generally performs better and is more efficient than RBDC for bursty traffic like HTTP. It directly tells the controller how much data needs to be sent.                                  |
| **FCA**        | Volume capacity assigned to terminals from bandwidth that would otherwise be unused. | - Best-effort background traffic                                                    | The controller distributes these resources proportionally based on active VBDC requests, avoiding waste on idle terminals.                                                                |

## Extracted QoS approaches
- DSCP-based classification (DiffServ):
The paper doesn't mention DSCP or DiffServ directly. However, it references the concept by citing another project, SATIP6, which described a QoS architecture "with the aim of differentiating IP flows to optimize resource utilization". The DAMA algorithm in this paper achieves a similar goal by using its own internal classes
- Use of priority queues:
This is the core QoS mechanism in the paper. The DAMA controller is built on a foundation of prioritization.
  - Request Classes: An RCST internally handles three types of request classes (RCs): real-time (RT), critical data (CD), and best effort (BE).
  - Assignment Hierarchy: The DAMA controller's bandwidth scheduling algorithm processes requests in a strict order of priority. It assigns bandwidth first to CRA, then to the RT class, then CD, and finally BE. Any remaining capacity can be distributed via FCA
This is a textbook example of using priority queues to enforce QoS. High-priority traffic (like RT) gets served first, ensuring its performance, while lower-priority traffic (like BE) gets what's left over.
