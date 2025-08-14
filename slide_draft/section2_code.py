import graphviz


def create_system_flow_diagram():
    """
    Creates and renders a diagram illustrating the DVB-S2X system flow,
    """
    # Create a new directed graph
    dot = graphviz.Digraph('SystemFlow', comment='System Flow Diagram')
    dot.attr(rankdir='LR', splines='line', nodesep='0.8')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the main nodes in the flow ---
    dot.node('internet', 'Internet', fillcolor='whitesmoke')
    dot.node('gateway', 'Gateway', fillcolor='lightblue')
    dot.node('satellite', 'Satellite\n(Bent Pipe)', shape='ellipse', fillcolor='lightyellow')
    dot.node('rcst', 'RCST Terminals', fillcolor='lightgreen')

    # --- Define the processes happening at the Gateway ---
    # Using an HTML-like table for better control over the layout and text.
    gateway_processes_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
  <TR>
    <TD BGCOLOR="lightcyan">GSE Encapsulation</TD>
    <TD BGCOLOR="lightcyan">Framing (BBFRAME → PLFRAME)</TD>
    <TD BGCOLOR="lightcyan">FEC and Modulation (MODCOD)</TD>
  </TR>
</TABLE>>'''
    dot.node('gateway_processes', gateway_processes_label, shape='plain')

    # --- Define the Edges for the main flow ---
    dot.edge('internet', 'gateway')
    dot.edge('gateway', 'satellite')
    dot.edge('satellite', 'rcst')

    # Connect the Gateway to its processes with a dashed line
    dot.edge('gateway', 'gateway_processes', style='dashed', arrowhead='none')

    # Render the graph to a file and open it automatically
    output_filename = 'system_flow_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_encapsulation_stack_diagram():
    """
    Creates and renders a diagram that visually represents the DVB-S2X
    encapsulation stack, from IP packets down to the PLFRAME.
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('EncapsulationStack', comment='DVB-S2X Encapsulation Stack')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over rows, columns, colors, and text formatting.
    stack_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
  <!-- Row 1: IP Packets -->
  <TR>
    <TD ALIGN="LEFT" BGCOLOR="white"><B>IP Packets</B></TD>
    <TD ALIGN="LEFT">← Application / IP Layer</TD>
  </TR>
  <!-- Row 2: GSE -->
  <TR>
    <TD ALIGN="LEFT" BGCOLOR="lightcyan"><B>GSE (Generic Stream Encapsulation)</B></TD>
    <TD></TD>
  </TR>
  <!-- Row 3: BBFRAME -->
  <TR>
    <TD ALIGN="LEFT" BGCOLOR="lightyellow">
      <B>BBFRAME (Baseband Frame)</B><BR/>
      [BBHEADER + GSE Packets]
    </TD>
    <TD></TD>
  </TR>
  <!-- Row 4: FEC -->
  <TR>
    <TD ALIGN="LEFT" BGCOLOR="#D4EDDA">
      <B>FEC (LDPC + BCH)</B><BR/>
      MODCOD applied (e.g., 8PSK, 16APSK)
    </TD>
    <TD></TD>
  </TR>
  <!-- Row 5: PLFRAME -->
  <TR>
    <TD ALIGN="LEFT" BGCOLOR="lightgreen">
      <B>PLFRAME (Physical Layer Frame)</B><BR/>
      [PLS Header + FEC-Protected Payload]
    </TD>
    <TD></TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('stack', stack_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'encapsulation_stack_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_encapsulation_diagram():
    """
    Creates and renders a diagram showing the encapsulation of IP packets
    into GSE packets and then into a BBFRAME.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('Encapsulation', comment='GSE and BBFRAME Encapsulation')
    dot.attr(rankdir='TB', splines='line', nodesep='1.0', ranksep='1.5')
    dot.attr('node', shape='plain', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Step 1: Generic Stream Encapsulation (GSE) ---
    # We use a cluster to create the grey box with a title.
    with dot.subgraph(name='cluster_gse') as c:
        c.attr(label='1. Generic Stream Encapsulation (GSE)', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='16')

        # Define the nodes within this cluster using HTML-like tables for structure.
        ip_packet_label = '<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0"><TR><TD WIDTH="150">IP Packet</TD></TR></TABLE>'
        c.node('ip_packet', ip_packet_label)

        gse_packet_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
  <TR>
    <TD BGCOLOR="lightblue">GSE Header</TD>
    <TD WIDTH="150">IP Packet</TD>
  </TR>
</TABLE>>'''
        c.node('gse_packet', gse_packet_label)

        # Arrow showing the encapsulation process
        c.edge('ip_packet', 'gse_packet', label='Wraps')

    # --- Step 2: Baseband Frame (BBFRAME) Grouping ---
    with dot.subgraph(name='cluster_bbframe') as c:
        c.attr(label='2. Baseband Frame (BBFRAME) Grouping', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='16')

        # Define the nodes for the second part of the flow.
        gse_packets_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
  <TR>
    <TD BGCOLOR="lightblue">GSE Packet 1</TD>
    <TD BGCOLOR="lightblue">GSE Packet 2</TD>
    <TD>...</TD>
  </TR>
</TABLE>>'''
        c.node('gse_packets', gse_packets_label)

        bbframe_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
  <TR>
    <TD BGCOLOR="lightyellow">BBHEADER</TD>
    <TD BGCOLOR="lightblue">GSE Packet 1</TD>
    <TD BGCOLOR="lightblue">GSE Packet 2</TD>
    <TD>...</TD>
  </TR>
</TABLE>>'''
        c.node('bbframe', bbframe_label)

        # Arrow showing the grouping process
        c.edge('gse_packets', 'bbframe', label='Grouped together with\na BBHEADER')

    # Render the graph to a file and open it automatically
    output_filename = 'gse_bbframe_encapsulation_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_fec_plframe_diagram():
    """
    Creates and renders a diagram showing how a BBFRAME is encoded
    with FEC and assembled into a PLFRAME for transmission.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('FEC_PLFRAME_Encoding', comment='FEC and PLFRAME Encoding Diagram')
    dot.attr(rankdir='TB', splines='line', nodesep='1.0', ranksep='1.2')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the Nodes in the Process ---
    dot.node('bbframe', 'BBFRAME', fillcolor='lightyellow')

    dot.node('fec_encoder',
             'FEC Encoder\n(LDPC + BCH)',
             fillcolor='lightblue')

    # Use a record shape to visually represent the structure of the PLFRAME
    plframe_label = ('{PLS Header |'
                     'FEC-Protected Payload\n(from encoded BBFRAME) |'
                     'Pilot Symbols}')
    dot.node('plframe', plframe_label, shape='record', fillcolor='lightgreen')

    dot.node('satellite', 'Satellite', shape='ellipse', fillcolor='lightyellow')

    # --- Define the Edges to Show the Flow ---
    dot.edge('bbframe', 'fec_encoder', label=' 1. Encoded by')

    dot.edge('fec_encoder', 'plframe',
             label=' 2. Assembled into PLFRAME')

    dot.edge('plframe', 'satellite',
             label=' 3. Transmitted via Satellite\n(using Adaptive Modulation/MODCOD)')

    # Render the graph to a file and open it automatically
    output_filename = 'fec_plframe_encoding_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_system_overview_diagram():
    """
    Creates and renders a diagram showing the DVB-RCS2 System Overview.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('SystemOverview', comment='DVB-RCS2 System Overview')
    dot.attr(rankdir='LR', splines='line', nodesep='0.8')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the Nodes ---
    # The nodes are defined with specific colors and text to match the visual.
    dot.node('internet', 'Internet', fillcolor='white')
    dot.node('gateway', 'Gateway', fillcolor='lightblue')
    dot.node('satellite', 'Satellite\n("Bent Pipe")', shape='ellipse', fillcolor='lightyellow')
    dot.node('rcst', 'RCST', fillcolor='lightgreen')
    dot.node('user_device', 'User Device', fillcolor='lightgreen')
    dot.node('ncc', 'NCC', fillcolor='lightblue')

    # --- Define the Edges (Connections) ---
    # Using dir='both' creates the double-sided arrows.
    dot.edge('internet', 'gateway', dir='both')
    dot.edge('gateway', 'satellite', dir='both')
    dot.edge('satellite', 'rcst', dir='both')
    dot.edge('rcst', 'user_device', dir='both')

    # This edge connects the Gateway down to the NCC.
    dot.edge('gateway', 'ncc')

    # Render the graph to a file and open it automatically
    output_filename = 'system_overview_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_ground_segment_diagram():
    """
    Creates and renders a diagram of the Ground Segment Breakdown,
    focusing on Gateway and NCC responsibilities.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('GroundSegment', comment='Ground Segment Breakdown')
    # Use compound=True to allow edges to connect to clusters cleanly
    dot.graph_attr.update(rankdir='LR', splines='line', nodesep='1.0', compound='true')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # Use a cluster to group the Gateway and NCC as the "Ground Segment"
    with dot.subgraph(name='cluster_ground') as c:
        c.attr(label='Ground Segment', style='filled', color='lightgrey', fontname='Helvetica', fontsize='14')
        c.node('gateway', 'Gateway - Modulates DVB-S2X', fillcolor='lightblue')
        c.node('ncc', 'NCC (Centralized Scheduler)', fillcolor='lightblue')

    # Define nodes outside the cluster
    dot.node('satellite', 'Satellite', shape='ellipse', fillcolor='lightyellow')
    dot.node('rcsts', 'RCSTs\n(User Terminals)', fillcolor='lightgreen')

    # Define the edges to show the communication flow
    # Using lhead/ltail with the cluster name ensures the arrows point to the box, not just a node
    dot.edge('gateway', 'satellite', label=' Forward Link')
    dot.edge('satellite', 'rcsts', label=' Downlink')
    dot.edge('rcsts', 'satellite', label=' Uplink (Return Link)')
    # This edge points from the satellite back to the NCC node inside the cluster
    dot.edge('satellite', 'ncc', label=' Feedback Loops / Scheduling Requests')

    # Render the graph to a file and open it automatically
    output_filename = 'ground_segment_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_rcst_functions_diagram():
    """
    Creates and renders a diagram illustrating the functions of an RCST
    in a DVB-RCS2.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('RCSTFunctions', comment='RCST Functions Diagram')
    dot.attr(splines='line', nodesep='1.0', ranksep='1.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # Define the central RCST node using an HTML-like table for detailed structure.
    # This allows for a title bar and a list of functions.
    rcst_label = '''<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
  <TR><TD BORDER="1" SIDES="B" BGCOLOR="lightgreen"><B>RCST (User Terminal)</B></TD></TR>
  <TR><TD BORDER="1" SIDES="LRTB" BGCOLOR="lightgreen" ALIGN="LEFT">
    - Receives control info (TPG, timing) from forward link<BR ALIGN="LEFT"/>
    - Requests access via return link<BR ALIGN="LEFT"/>
    - Transmits data using assigned timeslots<BR ALIGN="LEFT"/>
    - Adapts coding/modulation based on link budget<BR ALIGN="LEFT"/>
  </TD></TR>
</TABLE>>'''
    dot.node('rcst', rcst_label, shape='plain')

    # Define the other nodes
    dot.node('satellite', 'Satellite', shape='ellipse', fillcolor='lightyellow')
    dot.node('ncc', 'NCC', fillcolor='lightblue')

    # Define the edges to show the information flow
    dot.edge('satellite', 'rcst', label=' Inputs (TPG,\n timing info) ')
    dot.edge('rcst', 'satellite', label=' Outputs (Data bursts,\n access requests) ')

    # Dashed line for the feedback loop
    dot.edge('rcst', 'ncc', label=' Feedback /\n Access Requests ', style='dashed')

    # Render the graph to a file and open it automatically
    output_filename = 'rcst_functions_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_protocol_stack_diagram():
    """
    Creates and renders a diagram that visually represents the DVB-RCS2
    protocol stack
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('ProtocolStack', comment='DVB-RCS2 Protocol Stack')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over rows, colors, and text formatting.
    stack_label = '''<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="8">
  <!-- Row 1: Application Layer -->
  <TR>
    <TD ALIGN="CENTER" BGCOLOR="lightblue">
      <B>Application Layer</B><BR/>
      Application (e.g., VoIP, video, HTTP)
    </TD>
  </TR>
  <!-- Row 2: Transport Layer -->
  <TR>
    <TD ALIGN="CENTER" BGCOLOR="lightblue">
      <B>Transport Layer</B><BR/>
      Transport Layer (UDP / TCP)
    </TD>
  </TR>
  <!-- Row 3: Network Layer -->
  <TR>
    <TD ALIGN="CENTER" BGCOLOR="lightblue">
      <B>Network Layer</B><BR/>
      IP Layer
    </TD>
  </TR>
  <!-- Row 4: SI-SAP -->
  <TR>
    <TD ALIGN="CENTER" BGCOLOR="lightyellow">
      <B>SI-SAP (Convergence)</B><BR/>
      SI-SAP (Service Interface SAP)
    </TD>
  </TR>
  <!-- Row 5: MAC Layer -->
  <TR>
    <TD ALIGN="CENTER" BGCOLOR="lightyellow">
      <B>MAC Layer</B><BR/>
      MAC Layer (CRA/VBDC/DBRA, timing, QoS)
    </TD>
  </TR>
  <!-- Row 6: Physical Layer -->
  <TR>
    <TD ALIGN="CENTER" BGCOLOR="lightgreen">
      <B>Physical Layer</B><BR/>
      Physical Layer (DVB-RCS2 waveform)
    </TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('stack', stack_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'protocol_stack_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_mftdma_diagram():
    """
    Creates and renders a diagram illustrating the MF-TDMA structure
    and the composition of an RCST burst, matching the provided visual.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('MFTDMA_Visual', comment='MF-TDMA Diagram')
    dot.attr(rankdir='LR', splines='line', nodesep='2.0', ranksep='2.0')
    dot.attr('node', shape='plain', fontname='Helvetica')
    dot.attr(label='MF-TDMA (Multi-Frequency Time Division Multiple Access)', labelloc='b', fontsize='16')

    # --- Left Side: RCST Burst Structure ---
    # Use an HTML-like table to create the detailed burst structure.
    burst_label = '''<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="8">
  <TR><TD BORDER="1" COLSPAN="4">RCST Burst Structure</TD></TR>
  <TR>
    <TD BORDER="1" BGCOLOR="lightblue">Preamble</TD>
    <TD BORDER="1" BGCOLOR="lightyellow">Header</TD>
    <TD BORDER="1" BGCOLOR="lightgreen">Payload</TD>
    <TD BORDER="1" BGCOLOR="lightgrey">Guard Time</TD>
  </TR>
</TABLE>>'''
    dot.node('burst_structure', burst_label)

    # --- Right Side: MF-TDMA Grid ---
    # Use another HTML-like table to show time slots across different frequencies.
    mftdma_grid = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">
  <TR><TD BORDER="0" COLSPAN="5" ALIGN="CENTER">Time →</TD></TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 1</B></TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">RCST 1 Slot</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">RCST 2 Slot</TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">RCST 3 Slot</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">RCST 4 Slot</TD>
  </TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 2</B></TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">RCST 3 Slot</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">RCST 1 Slot</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">RCST 4 Slot</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">RCST 2 Slot</TD>
  </TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 3</B></TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">RCST 2 Slot</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">RCST 4 Slot</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">RCST 1 Slot</TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">RCST 3 Slot</TD>
  </TR>
</TABLE>>'''
    dot.node('mftdma_grid', mftdma_grid)

    # We don't need an edge, as they are two parts of one conceptual diagram.
    # Graphviz will place them side-by-side due to the rankdir='LR' setting.

    # Render the graph to a file and open it automatically
    output_filename = 'mftdma_visual_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_qos_scheduling_diagram():
    """
    Creates and renders a diagram illustrating QoS and Scheduling
    in a DVB-RCS2 system, matching the provided visual.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('QoS_Scheduling', comment='QoS and Scheduling Diagram')
    dot.attr(rankdir='TB', splines='line', nodesep='1.2', ranksep='1.2')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Top Cluster: User Terminals (RCSTs) ---
    with dot.subgraph(name='cluster_rcsts') as c:
        c.attr(label='User Terminals (RCSTs)', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')
        c.node('rcst1', 'RCST 1\n(Real-Time: VoIP)', fillcolor='#FFCCCC')
        c.node('rcst2', 'RCST 2\n(Elastic: Web Traffic)', fillcolor='#FFF3CD')
        c.node('rcst3', 'RCST 3\n(Streaming: Video)', fillcolor='#CCE5FF')

    # --- Middle Node: NCC (Centralized Scheduler) ---
    # Use an HTML-like table for the complex layout.
    ncc_label = '''<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
  <TR><TD COLSPAN="2" BGCOLOR="lightblue"><B>NCC (Centralized Scheduler)</B></TD></TR>
  <TR>
    <TD BORDER="1" ALIGN="RIGHT">Adapts to:</TD>
    <TD BORDER="1" ALIGN="LEFT">
      - Terminal Demand (Data Backlog)<BR ALIGN="LEFT"/>
      - Link Quality (SNR Feedback)<BR ALIGN="LEFT"/>
      - Priority Classes (QoS)<BR ALIGN="LEFT"/>
    </TD>
  </TR>
</TABLE>>'''
    dot.node('ncc', ncc_label, shape='plain')

    # --- Bottom Node: Return Link (MF-TDMA Grid) ---
    mftdma_grid_label = '''<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
  <TR><TD COLSPAN="5" BGCOLOR="whitesmoke"><B>Return Link (MF-TDMA Grid)</B></TD></TR>
  <TR><TD BORDER="0" COLSPAN="5" ALIGN="CENTER">Time →</TD></TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 1</B></TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">VoIP</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">Video</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">VoIP</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">Web</TD>
  </TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 2</B></TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">Video</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">VoIP</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">Video</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">VoIP</TD>
  </TR>
</TABLE>>'''
    dot.node('mftdma_grid', mftdma_grid_label, shape='plain')

    # --- Edges and Labels ---
    dot.edge('rcst1', 'ncc', label=' Access Request (DRA)\n[High Priority, Low Latency] ')
    dot.edge('rcst2', 'ncc', label=' Access Request (DRA)\n[Best Effort] ')
    dot.edge('rcst3', 'ncc', label=' Access Request (DRA)\n[Sustained Throughput] ')
    dot.edge('ncc', 'mftdma_grid', label=' Assigns Time-Frequency Slots ')

    # Render the graph to a file and open it automatically
    output_filename = 'qos_scheduling_visual_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")
    
# Run the function to create the diagram
if __name__ == "__main__":
    pass
