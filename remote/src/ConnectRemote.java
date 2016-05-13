import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.net.InetAddress;
import java.awt.event.ActionEvent;

public class ConnectRemote {

	private JFrame frmTellusRover;
	private JTextField textIP;
	private JTextField textControlPort;
	private JTextField textVideoPort;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ConnectRemote window = new ConnectRemote();
					window.frmTellusRover.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}
	
	
	public static String prepareToConnect(String strIP, String strControlPort, String strVideoPort)
	{
		boolean inputIsValid = true;
		
		try{
			InetAddress deviceIP = InetAddress.getByName(strIP);
		} catch (Exception e){
			return "Invalid value for 'IP': " + strIP;
		}
		
		int ControlPort = -1;
		boolean invControlPort = false;
		try{
			ControlPort = Integer.parseInt(strControlPort);
		} catch(Exception e){
			invControlPort = true;
		}
		if (invControlPort == false){
			if (ControlPort < 0 | ControlPort >= 65536){
				invControlPort = true;
			}
		}
		if (invControlPort)
			return "Invalid value for 'Control Port': " + strControlPort;
		
		
		int VideoPort = -1;
		boolean invVideoPort = false;
		try{
			VideoPort = Integer.parseInt(strVideoPort);
		} catch(Exception e){
			invVideoPort = true;
		}
		if (invVideoPort == false){
			if (VideoPort < 0 | VideoPort >= 65536){
				invVideoPort = true;
			}
		}
		if (invVideoPort)
			return "Invalid value for 'Video Port': " + strVideoPort;
		
		
		return "";
	}
	
	
	

	/**
	 * Create the application.
	 */
	public ConnectRemote() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmTellusRover = new JFrame();
		frmTellusRover.setTitle("Tellus Rover - Connect");
		frmTellusRover.setBounds(100, 100, 298, 190);
		frmTellusRover.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmTellusRover.getContentPane().setLayout(null);
		
		JLabel lblIp = new JLabel("IP:");
		lblIp.setBounds(10, 11, 81, 14);
		frmTellusRover.getContentPane().add(lblIp);
		
		JLabel lblRemotePort = new JLabel("Control Port:");
		lblRemotePort.setBounds(10, 36, 81, 14);
		frmTellusRover.getContentPane().add(lblRemotePort);
		
		JLabel lblCamera = new JLabel("Video port:");
		lblCamera.setBounds(10, 61, 81, 14);
		frmTellusRover.getContentPane().add(lblCamera);
		
		textIP = new JTextField();
		textIP.setBounds(101, 8, 171, 20);
		frmTellusRover.getContentPane().add(textIP);
		textIP.setColumns(10);
		
		textControlPort = new JTextField();
		textControlPort.setBounds(101, 33, 171, 20);
		frmTellusRover.getContentPane().add(textControlPort);
		textControlPort.setColumns(10);
		
		textVideoPort = new JTextField();
		textVideoPort.setToolTipText("");
		textVideoPort.setBounds(101, 58, 171, 20);
		frmTellusRover.getContentPane().add(textVideoPort);
		textVideoPort.setColumns(10);
		
		JButton btnSetDefaults = new JButton("Set Defaults");
		btnSetDefaults.setBounds(10, 123, 132, 23);
		frmTellusRover.getContentPane().add(btnSetDefaults);
		
		JButton btnLoadDefaults = new JButton("Load Defaults");
		btnLoadDefaults.setBounds(152, 123, 120, 23);
		frmTellusRover.getContentPane().add(btnLoadDefaults);
		
		JButton btnConnect = new JButton("Connect");
		btnConnect.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String strValid = prepareToConnect(textIP.getText(),
						textControlPort.getText(),
						textVideoPort.getText());
				if (!strValid.isEmpty()){
					JOptionPane.showMessageDialog(null, strValid, "Validation Error", JOptionPane.WARNING_MESSAGE);
				}
			}
		});
		btnConnect.setBounds(10, 86, 262, 26);
		frmTellusRover.getContentPane().add(btnConnect);
	}
}
