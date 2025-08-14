import graphviz


def create_l1_framing_comparison_diagram():
    """
    Creates and renders a diagram that visually compares the frame structures
    of DVB-S2X and DVB-RCS2.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('L1_Framing_Comparison', comment='L1 Framing Comparison Diagram')
    dot.attr(rankdir='TB', nodesep='1.0')  # Top-to-Bottom layout
    dot.attr('node', shape='plain', fontname='Helvetica')

    # --- DVB-RCS2 (Return) Visual ---
    # Use an HTML-like table to create the complex nested structure.
    rcs2_label = '''<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" STYLE="rounded">
  <TR><TD BORDER="0" ALIGN="CENTER">DVB-RCS2 (Return)</TD></TR>
  <TR><TD BORDER="0">
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
      <TR>
        <TD BGCOLOR="lightyellow">DVB-RCS2</TD>
        <TD BGCOLOR="lightyellow">Burst Slot</TD>
        <TD BGCOLOR="lightyellow" BORDER="0">
          <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR><TD>Preamble</TD></TR>
            <TR><TD>Payload</TD></TR>
            <TR><TD>Guard</TD></TR>
          </TABLE>
        </TD>
      </TR>
    </TABLE>
  </TD></TR>
</TABLE>>'''
    dot.node('rcs2_frame', rcs2_label)

    # --- DVB-S2X (Forward) Visual ---
    s2x_label = '''<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" STYLE="rounded">
  <TR><TD BORDER="0" ALIGN="CENTER">DVB-S2X (Forward)</TD></TR>
  <TR><TD BORDER="0">
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
      <TR>
        <TD BGCOLOR="lightgreen">DVB-S2X</TD>
        <TD BGCOLOR="lightgreen">PLFRAME</TD>
        <TD BGCOLOR="lightgreen" BORDER="0">
          <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR><TD>Header</TD></TR>
            <TR><TD>Payload</TD></TR>
            <TR><TD>Pilots</TD></TR>
          </TABLE>
        </TD>
      </TR>
    </TABLE>
  </TD></TR>
</TABLE>>'''
    dot.node('s2x_frame', s2x_label)

    # Render the graph to a file and open it automatically
    output_filename = 'l1_framing_comparison_visual'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_bbframe_structure_diagram():
    """
    Creates and renders a diagram showing the structure of a BBFRAME.
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('BBFRAME_Structure', comment='BBFRAME Structure Diagram')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over cells, borders, and colors.
    bbframe_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
  <TR>
    <TD BGCOLOR="lightyellow"><B>BBHEADER</B></TD>
    <TD BGCOLOR="lightblue">GSE Packet 1</TD>
    <TD BGCOLOR="lightblue">GSE Packet 2</TD>
    <TD BGCOLOR="lightblue">GSE Packet 3</TD>
    <TD>...</TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('bbframe', bbframe_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'bbframe_structure_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_fec_pipeline_diagram():
    """
    Creates and renders a diagram showing the two-stage FEC encoding pipeline.
    """
    # Create a new directed graph, laying it out from Left to Right.
    dot = graphviz.Digraph('FEC_Pipeline', comment='FEC Pipeline Diagram')
    dot.attr(rankdir='LR', splines='line')
    dot.attr('node', shape='box', style='filled', fontname='Helvetica')
    dot.attr('edge', style='solid')

    # --- Define the Nodes in the Pipeline ---
    # The nodes are defined with specific colors to match the visual.
    dot.node('bbframe', 'BBFRAME', fillcolor='white')
    dot.node('ldpc', 'LDPC Encoder', fillcolor='lightblue')
    dot.node('bch', 'BCH Encoder', fillcolor='lightgreen')
    dot.node('payload', 'FEC - Protected Payload', fillcolor='lightyellow')

    # --- Define the Edges to Show the Flow ---
    dot.edge('bbframe', 'ldpc')
    dot.edge('ldpc', 'bch')
    dot.edge('bch', 'payload')

    # --- Add the Bottom Caption ---
    caption = (
        '\nDVB-S2X uses a two-stage FEC system to protect data: LDPC for powerful error correction, and BCH for outer cleaning and detection.\n'
        'This ensures reliable transmission over satellite links.')
    dot.attr(label=caption, labelloc='b', fontsize='12', fontname='Helvetica')

    # Render the graph to a file and open it automatically
    output_filename = 'fec_pipeline_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_plframe_diagram():
    """
    Creates and renders a diagram showing the structure and purpose
    of the DVB-S2X PLFRAME.
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('PLFRAME_Structure', comment='PLFRAME Structure Diagram')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over the layout, colors, and text.
    plframe_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="8">
  <!-- Top row with the main components -->
  <TR>
    <TD BORDER="1" BGCOLOR="lightblue">PLS Header</TD>
    <TD BORDER="1" BGCOLOR="lightyellow">FEC-Protected BBFRAME</TD>
    <TD BORDER="1" BGCOLOR="lightgreen">Pilot Symbols</TD>
  </TR>
  <!-- Row with arrows -->
  <TR>
    <TD BORDER="0" ALIGN="CENTER">↓</TD>
    <TD BORDER="0" ALIGN="CENTER">↓</TD>
    <TD BORDER="0" ALIGN="CENTER">↓</TD>
  </TR>
  <!-- Bottom row with explanatory text -->
  <TR>
    <TD BORDER="0" ALIGN="CENTER">Decoder Info<BR/>(MODCOD, Frame Type)</TD>
    <TD BORDER="0" ALIGN="CENTER">Actual User Data</TD>
    <TD BORDER="0" ALIGN="CENTER">Synchronization &amp;<BR/>Signal Tracking</TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('plframe', plframe_label)

    # Render the graph to a file and open it automatically
    output_filename = 'plframe_structure_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_modcod_mapping_diagram():
    """
    Creates and renders a diagram showing the MODCOD Mapping Table.
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('MODCOD_Mapping', comment='MODCOD Mapping Table Diagram')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over rows, columns, borders, and colors.
    modcod_table_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
  <!-- Header Row -->
  <TR>
    <TD BGCOLOR="lightgrey"><B>SNR Range (dB)</B></TD>
    <TD BGCOLOR="lightgrey"><B>Modulation</B></TD>
    <TD BGCOLOR="lightgrey"><B>Coding Rate</B></TD>
    <TD BGCOLOR="lightgrey"><B>MODCOD Name</B></TD>
  </TR>
  <!-- Data Rows -->
  <TR>
    <TD>&lt; 3 dB</TD>
    <TD>QPSK</TD>
    <TD>1/4</TD>
    <TD>MODCOD 1</TD>
  </TR>
  <TR>
    <TD>3-5 dB</TD>
    <TD>QPSK</TD>
    <TD>1/2</TD>
    <TD>MODCOD 2</TD>
  </TR>
  <TR>
    <TD>5-7 dB</TD>
    <TD>8PSK</TD>
    <TD>2/3</TD>
    <TD>MODCOD 6</TD>
  </TR>
  <TR>
    <TD>7-10 dB</TD>
    <TD>16APSK</TD>
    <TD>3/4</TD>
    <TD>MODCOD 12</TD>
  </TR>
  <TR>
    <TD>10-13 dB</TD>
    <TD>32APSK</TD>
    <TD>4/5</TD>
    <TD>MODCOD 17</TD>
  </TR>
  <TR>
    <TD>&gt; 13 dB</TD>
    <TD>64APSK</TD>
    <TD>5/6</TD>
    <TD>MODCOD 23</TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('modcod_table', modcod_table_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'modcod_mapping_table_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_superframe_diagram():
    """
    Creates and renders a diagram showing the DVB-S2X Superframe structure
    for a multi-beam scenario.
    """
    # Create a new directed graph. We will use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('Superframe_Structure', comment='DVB-S2X Superframe Diagram')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over the layout, colors, and text.
    superframe_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="8" CELLPADDING="0">
  <!-- Title Row -->
  <TR>
    <TD BORDER="0"></TD>
    <TD BORDER="0" COLSPAN="6" ALIGN="CENTER">
      <B>Time →</B><BR/>
      <FONT POINT-SIZE="16">Superframe</FONT>
    </TD>
  </TR>
  <!-- Beam A Row -->
  <TR>
    <TD ALIGN="RIGHT"><B>Beam A:</B></TD>
    <TD>
      <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
        <TR>
          <TD BGCOLOR="orange">SoSF</TD>
          <TD BGCOLOR="lightblue">PL</TD>
          <TD BGCOLOR="lightgrey">P</TD>
          <TD BGCOLOR="lightblue">PL</TD>
          <TD BGCOLOR="lightgrey">P</TD>
          <TD BGCOLOR="lightblue">PL</TD>
        </TR>
      </TABLE>
    </TD>
  </TR>
  <!-- Beam B Row -->
  <TR>
    <TD ALIGN="RIGHT"><B>Beam B:</B></TD>
    <TD>
      <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
        <TR>
          <TD BGCOLOR="orange">SoSF</TD>
          <TD BGCOLOR="lightblue">PL</TD>
          <TD BGCOLOR="lightgrey">P</TD>
          <TD BGCOLOR="lightblue">PL</TD>
          <TD BGCOLOR="lightgrey">P</TD>
          <TD BGCOLOR="lightblue">PL</TD>
        </TR>
      </TABLE>
    </TD>
  </TR>
  <!-- Legend Row -->
  <TR>
    <TD BORDER="0"></TD>
    <TD BORDER="0" COLSPAN="6" ALIGN="LEFT">
      <BR/><BR/>
      <B>Legend:</B><BR ALIGN="LEFT"/>
      SoSF = Start of Superframe<BR ALIGN="LEFT"/>
      PL = PLFRAME<BR ALIGN="LEFT"/>
      P = Pilot<BR ALIGN="LEFT"/>
    </TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('superframe', superframe_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'superframe_structure_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_rcs2_burst_diagram():
    """
    Creates and renders a diagram showing the DVB-RCS2 burst structure
    and how multiple RCSTs share the return link.
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('RCS2_Burst_Structure', comment='DVB-RCS2 Burst Structure Diagram')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over the layout, colors, and text.
    burst_stack_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="8" CELLPADDING="0">
  <!-- RCST 1 Row with details -->
  <TR>
    <TD>
      <TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
        <TR>
          <TD BORDER="1" BGCOLOR="lightblue">Preamble</TD>
          <TD BORDER="1" BGCOLOR="lightcyan">Header</TD>
          <TD BORDER="1" BGCOLOR="lightgreen">Payload</TD>
          <TD BORDER="1" BGCOLOR="lightgrey">Guard</TD>
        </TR>
        <TR>
          <TD BORDER="0" ALIGN="CENTER">↓<BR/>Sync</TD>
          <TD BORDER="0" ALIGN="CENTER">↓<BR/>Identity</TD>
          <TD BORDER="0" ALIGN="CENTER">↓<BR/>User Data</TD>
          <TD BORDER="0" ALIGN="CENTER">↓<BR/>Delay Buffer</TD>
        </TR>
      </TABLE>
    </TD>
    <TD VALIGN="MIDDLE">RCST 1</TD>
  </TR>
  <!-- RCST 2 Row -->
  <TR>
    <TD>
      <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
        <TR>
          <TD BGCOLOR="lightblue">Preamble</TD>
          <TD BGCOLOR="lightcyan">Header</TD>
          <TD BGCOLOR="lightgreen">Payload</TD>
          <TD BGCOLOR="lightgrey">Guard</TD>
        </TR>
      </TABLE>
    </TD>
    <TD VALIGN="MIDDLE">RCST 2</TD>
  </TR>
  <!-- RCST 3 Row -->
  <TR>
    <TD>
      <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
        <TR>
          <TD BGCOLOR="lightblue">Preamble</TD>
          <TD BGCOLOR="lightcyan">Header</TD>
          <TD BGCOLOR="lightgreen">Payload</TD>
          <TD BGCOLOR="lightgrey">Guard</TD>
        </TR>
      </TABLE>
    </TD>
    <TD VALIGN="MIDDLE">RCST 3</TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('burst_stack', burst_stack_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'rcs2_burst_structure_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_burst_grid_diagram():
    """
    Creates and renders a diagram showing the MF-TDMA burst grid,
    illustrating how multiple RCSTs share the return link.
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('Burst_Grid_Overview', comment='MF-TDMA Burst Grid Diagram')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over the layout, colors, and text.
    burst_grid_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">
  <TR><TD BORDER="0" COLSPAN="5" ALIGN="CENTER"><B>Time →</B></TD></TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 1</B></TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">RCST 1</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">RCST 2</TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">RCST 3</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">RCST 4</TD>
  </TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 2</B></TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">RCST 3</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">RCST 1</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">RCST 4</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">RCST 2</TD>
  </TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 3</B></TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">RCST 2</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">RCST 4</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">RCST 1</TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">RCST 3</TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('burst_grid', burst_grid_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'burst_grid_overview_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_assignment_methods_diagram():
    """
    Creates and renders a diagram comparing Scheduled and Contention-Based
    slot assignment methods in DVB-RCS2.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('AssignmentMethods', comment='Slot Assignment Methods Diagram')
    dot.attr(rankdir='TB', nodesep='1.0', ranksep='1.0')  # Top-to-Bottom layout
    dot.attr('node', shape='plain', fontname='Helvetica')

    # --- 1. Contention Access Visual ---
    # Use an HTML-like table within a cluster to create the visual.
    with dot.subgraph(name='cluster_contention') as c:
        c.attr(label='Contention Access', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')

        contention_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">
  <TR><TD BORDER="0" COLSPAN="3" ALIGN="CENTER"><B>Time →</B></TD></TR>
  <TR>
    <TD BORDER="1" BGCOLOR="#FFF3CD">Request</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">Reserved</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">Request</TD>
  </TR>
  <TR>
    <TD BORDER="1" BGCOLOR="#FFCCCC">Reserved</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">Request</TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">Reserved</TD>
  </TR>
</TABLE>>'''
        c.node('contention_grid', contention_label)

    # --- 2. Scheduled Access Visual ---
    with dot.subgraph(name='cluster_scheduled') as c:
        c.attr(label='Scheduled Access', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')

        scheduled_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">
  <TR><TD BORDER="0" COLSPAN="3" ALIGN="CENTER"><B>Time →</B></TD></TR>
  <TR>
    <TD BORDER="1" BGCOLOR="#FFCCCC">RCST 1</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">RCST 2</TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">RCST 3</TD>
  </TR>
  <TR>
    <TD BORDER="1" BGCOLOR="#FFCCCC">RCST 1</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">RCST 2</TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">RCST 3</TD>
  </TR>
</TABLE>>'''
        c.node('scheduled_grid', scheduled_label)

    # Render the graph to a file and open it automatically
    output_filename = 'assignment_methods_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_return_burst_timing_diagram():
    """
    Creates and renders a diagram showing the RCST Return Burst Timing
    in an MF-TDMA grid.
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('ReturnBurstTiming', comment='RCST Return Burst Timing Diagram')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over the layout, colors, and text.
    timing_grid_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
  <!-- Header Row for Time Slots -->
  <TR>
    <TD BORDER="0"></TD>
    <TD BORDER="0" ALIGN="CENTER"><B>Time Slot 1</B></TD>
    <TD BORDER="0" ALIGN="CENTER"><B>Time Slot 2</B></TD>
    <TD BORDER="0" ALIGN="CENTER"><B>Time Slot 3</B></TD>
  </TR>
  <!-- Frequency 1 Row -->
  <TR>
    <TD ALIGN="RIGHT"><B>Freq 1</B></TD>
    <TD BGCOLOR="#FFCCCC">
      <B>RCST 1</B><BR/>
      Preamble + Payload + Guard
    </TD>
    <TD BGCOLOR="whitesmoke"></TD>
    <TD BGCOLOR="#D4EDDA">
      <B>RCST 3</B><BR/>
      Preamble + Payload + Guard
    </TD>
  </TR>
  <!-- Frequency 2 Row -->
  <TR>
    <TD ALIGN="RIGHT"><B>Freq 2</B></TD>
    <TD BGCOLOR="whitesmoke"></TD>
    <TD BGCOLOR="#CCE5FF">
      <B>RCST 2</B><BR/>
      Preamble + Payload + Guard
    </TD>
    <TD BGCOLOR="whitesmoke"></TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('timing_grid', timing_grid_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'rcst_return_burst_timing_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_rcs2_modcod_table_diagram():
    """
    Creates and renders a diagram showing the DVB-RCS2 MODCOD Table,
    visually representing the trade-off between robustness and throughput.
    """
    # Create a new directed graph. We'll use a single node with an
    # HTML-like table for precise layout control.
    dot = graphviz.Digraph('RCS2_MODCOD_Table', comment='DVB-RCS2 MODCOD Table Diagram')
    dot.attr('node', shape='plain', fontname='Helvetica')

    # Define the entire visual as an HTML-like table.
    # This gives us full control over the layout, colors, and text.
    modcod_table_label = '''<
<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
  <!-- Header Row -->
  <TR>
    <TD BGCOLOR="lightgrey"><B>Modulation</B></TD>
    <TD BGCOLOR="lightgrey"><B>Code Rate</B></TD>
    <TD BGCOLOR="lightgrey"><B>Description</B></TD>
  </TR>
  <!-- Data Rows -->
  <TR>
    <TD>QPSK</TD>
    <TD>1/3</TD>
    <TD BGCOLOR="#FFCCCC">Very robust, low data rate</TD>
  </TR>
  <TR>
    <TD>QPSK</TD>
    <TD>2/3</TD>
    <TD BGCOLOR="#FFF3CD">Balanced</TD>
  </TR>
  <TR>
    <TD>8PSK</TD>
    <TD>3/4</TD>
    <TD BGCOLOR="#D4EDDA">Higher data rate</TD>
  </TR>
  <TR>
    <TD>16QAM</TD>
    <TD>7/8</TD>
    <TD BGCOLOR="#CCE5FF">Max throughput (needs strong signal)</TD>
  </TR>
</TABLE>>'''

    # Create a single node that contains the entire table structure.
    dot.node('modcod_table', modcod_table_label)

    # Render the graph to a file and open it automatically.
    output_filename = 'rcs2_modcod_table_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_e2e_flow_diagram():
    """
    Creates and renders a diagram showing the end-to-end data flow
    for both DVB-S2X (Forward) and DVB-RCS2 (Return) links.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('E2E_Flow', comment='End-to-End Flow Diagram')
    dot.attr(rankdir='TB', splines='line', nodesep='0.8', ranksep='1.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Forward Link (DVB-S2X) Subgraph ---
    with dot.subgraph(name='cluster_forward') as c:
        c.attr(label='Forward Link (DVB-S2X): Gateway → User Terminal', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightblue')
        # Define the nodes in the forward flow
        c.node('ip', 'IP Packets')
        c.node('gse', 'GSE Packets')
        c.node('bbframe', 'BBFRAME')
        c.node('fec', 'FEC (LDPC+BCH)')
        c.node('plframe', 'PLFRAME')
        c.node('superframe', 'Superframe')
        # Connect the nodes to show the flow
        c.edge('ip', 'gse', label='Wrapped')
        c.edge('gse', 'bbframe', label='Grouped')
        c.edge('bbframe', 'fec', label='Protected')
        c.edge('fec', 'plframe', label='Encapsulated')
        c.edge('plframe', 'superframe', label='Multiplexed')

    # --- Return Link (DVB-RCS2) Subgraph ---
    with dot.subgraph(name='cluster_return') as c:
        c.attr(label='Return Link (DVB-RCS2): User Terminal → Gateway', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightgreen')
        # Define the nodes in the return flow
        c.node('rcst', 'RCST')
        c.node('burst', 'Burst\n(Preamble+Header+Payload+Guard)')
        c.node('tdma', 'MF-TDMA Slot')
        c.node('gateway_hub', 'Gateway Hub')
        # Connect the nodes to show the flow
        c.edge('rcst', 'burst', label='Frames Data')
        c.edge('burst', 'tdma', label='Transmits in')
        c.edge('tdma', 'gateway_hub', label='Received by')

    # Render the graph to a file and open it automatically
    output_filename = 'e2e_flow_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


# Run the function to create the diagram
if __name__ == "__main__":
    pass
