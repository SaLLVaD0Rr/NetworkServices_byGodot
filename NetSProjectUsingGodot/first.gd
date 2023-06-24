extends Control

@onready var played = false
var nmaptrigger = false


func _ready():
	$AnimationPlayer.play_backwards("Switch")
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func play():
	if played == false:
		$AnimationPlayer.play("disperse")
		played = true
	elif played == true:
		pass



func _on_back_pressed():
	get_tree().change_scene_to_file("res://control.tscn")


func _on_networking_toggle_pressed():
	$AnimationPlayer.play("Switch")
	await get_tree().create_timer(0.3).timeout 
	get_tree().change_scene_to_file("res://networking.tscn")


func _on_organization_pressed():
	$AnimationPlayer.play("Switch")
	await get_tree().create_timer(0.3).timeout 
	get_tree().change_scene_to_file("res://organisation.tscn")
