"""Subclass of CameraDialog, which is generated by wxFormBuilder."""

import gui
import mainaction

# Implementing CameraDialog
class DialogFrame( gui.CameraDialog ):
	device = -1
	def __init__( self, parent ):
		gui.CameraDialog.__init__( self, parent )

	# Handlers for CameraDialog events.
	def OnOk( self, event ):
		# TODO: Implement OnOk
		DialogFrame.device = self.search[self.CameraCombobox.GetValue()]
		self.Close(True)
