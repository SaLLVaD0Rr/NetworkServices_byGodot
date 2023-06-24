extends HSlider

signal send_msg
# Called when the node enters the scene tree for the first time.
func _ready():
	pass
	
func _physics_process(delta):
	if value == 50:
		emit_signal("send_msg")
