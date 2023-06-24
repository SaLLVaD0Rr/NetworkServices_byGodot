extends Control

var new_scene = load("res://first.tscn")

# Called when the node enters the scene tree for the first time.
func _ready():
	$AnimationPlayer.play_backwards("Switch")
	$AnimationPlayer.play("logo")
	
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass



func switching():
	get_tree().change_scene_to_file("res://first.tscn")

func _on_learn_pressed():
	$AnimationPlayer.play("Switch")
	$AnimationPlayer.play_backwards("logo")
	await get_tree().create_timer(0.3).timeout
	switching()
	
	
	
	

