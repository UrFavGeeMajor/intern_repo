### MPLS-Based Pathing in Satellite Networks
Multi-Protocol Label Switching (MPLS) is a high-performance network routing technique. Instead of looking up a complex destination IP address at every hop, routers use a simple, short "label" that's attached to the packet.
Think of it like this: Standard IP routing is like a mail sorter having to read a full, detailed address on every letter at every post office. MPLS is like putting a simple barcode on the letter at the first post office; every subsequent sorter just scans the barcode to know exactly which bin to throw it in, which is much faster.

### LSP Setup Logic
The "path" or "tunnel" that labeled packets travel through is called a Label Switched Path (LSP).
- What it is: An LSP is a pre-determined, one-way path from an ingress (entry) router to an egress (exit) router across the MPLS network.
- How it's built: When a data packet that needs special handling arrives at the network edge, the ingress router identifies its type (e.g., voice traffic). It then uses a signaling protocol—typically RSVP-TE (Resource Reservation Protocol with Traffic Engineering) in complex networks—to ask the next router in the desired path, "What label should I use for this kind of traffic going to you?" That router then asks the next one, and so on, until the entire path is established. Once set up, all similar packets are "pushed" onto this LSP.
In a satellite context, these LSPs aren't usually set up on-demand. They are often pre-established by the network operations center.

### Differentiation by Service Class (EF, AF, BE)
This is the Quality of Service (QoS) component of MPLS, which works hand-in-hand with the Differentiated Services (DiffServ) model. LSPs are created to provide different levels of service:
- 🥇 EF (Expedited Forwarding): This is the "first-class" lane for high-priority traffic that cannot tolerate delay, like VoIP or real-time command and control. An LSP engineered for EF traffic will be routed over the fastest, most reliable links with guaranteed bandwidth.
= 🥈 AF (Assured Forwarding): This is the "business-class" lane for important traffic that needs reliable delivery but can handle some delay, like streaming video or critical business applications. These LSPs guarantee a certain minimum bandwidth.
- 🥉 BE (Best Effort): This is the "economy" lane for everything else—general web Browse, non-critical file transfers, etc. This traffic uses whatever capacity is left over.
The ingress router inspects incoming packets, maps them to one of these classes based on their IP header, and directs them onto the appropriate pre-built LSP.

### How Satellite Systems Implement Pre-defined Routes
In dynamic terrestrial networks, routing protocols are constantly finding new paths. Satellite networks, especially those with expensive space assets, are often more rigidly controlled.
- Centralized Control: The Network Operations Center (NOC) or Network Control Center (NCC) acts as the all-seeing eye. It has a complete and static view of the entire network: the positions of all satellites, the status of inter-satellite links (ISLs), and the load on all ground gateways.
- Traffic Engineering (TE): Using this global view, network engineers pre-calculate and pre-define the most optimal routes for different types of traffic between various points. These engineered paths become the LSPs. For example, the NOC can create a permanent, low-latency LSP for a major client that snakes through specific satellites from Europe to North America.
- Static by Design: This pre-defined route (the LSP) remains static unless there's a component failure or the NOC purposefully re-routes traffic to manage overall network load. This provides predictable performance and avoids the overhead and potential instability of dynamic routing protocols operating over long-delay satellite links.



