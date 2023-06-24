extends Control



var interpret_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/venv/Scripts/python.exe")
var nmap_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_nmap.py")
var lanscan_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_lanscan.py")
var nslook_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_nslook.py")
var renew_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_renew.py")
var qr_path =ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_qr.py")
var pass_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_wifi_pass.py")
var dns_path  = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_dns.py")
var webstat_path = ProjectSettings.globalize_path("res://Pythonfiles/cripts/launch_web_stat.py")


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_back_pressed():
	get_tree().change_scene_to_file("res://first.tscn")


func _on_launch_nmap_pressed():
	OS.execute(interpret_path,[nmap_path])


func _on_launch_lanscan_pressed():
	OS.execute(interpret_path,[lanscan_path])


func _on_launch_nslook_pressed():
	OS.execute(interpret_path,[nslook_path])


func _on_launch_web_stat_pressed():
	OS.execute(interpret_path,[webstat_path])


func _on_launch_renew_pressed():
	OS.execute(interpret_path,[renew_path])


func _on_launch_dns_pressed():
	OS.execute(interpret_path,[dns_path])


func _on_launch_qr_pressed():
	OS.execute(interpret_path,[qr_path])


func _on_launch_pass_pressed():
	OS.execute(interpret_path,[pass_path])
