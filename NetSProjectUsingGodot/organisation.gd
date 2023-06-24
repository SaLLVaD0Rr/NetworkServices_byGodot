extends Control


var DIR = OS.get_executable_path().get_base_dir()

var interpret_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/venv/Scripts/python.exe")
var image_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_images.py")
var file_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_organize.py")
var dedup_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_dedup.py")
var website_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_web_avail.py")
var pass_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_generate.py")

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_back_pressed():
	get_tree().change_scene_to_file("res://first.tscn")


func _on_launch_image_pressed():
	OS.execute(interpret_path,[image_path])


func _on_launch_file_pressed():
	OS.execute(interpret_path,[file_path])


func _on_launch_dedup_pressed():
	OS.execute(interpret_path,[dedup_path])


func _on_launch_web_pressed():
	OS.execute(interpret_path,[website_path])


func _on_launch_pass_pressed():
	OS.execute(interpret_path,[pass_path])
