import gdsfactory as gf

@gf.cell
def cam_pram_cell_grid():
    c = gf.Component("CAM_PRAM_ARRAY")
    
    led_surrogate = gf.components.straight(length=10, width=0.5)
    detector_surrogate = gf.components.straight(length=10, width=0.5)
    optical_path = gf.components.coupler_ring(radius=5, gap=0.2)

    spacing_x = 30
    spacing_y = 30

    for i in range(4):
        for j in range(4):
            x_pos = i * spacing_x
            y_pos = j * spacing_y
            
            led_ref = c << led_surrogate
            led_ref.move((x_pos, y_pos))
            
            path_ref = c << optical_path
            path_ref.move((x_pos + 10, y_pos + 5))
            
            det_ref = c << detector_surrogate
            det_ref.move((x_pos + 20, y_pos))

    return c

if __name__ == "__main__":
    mem_array = cam_pram_cell_grid()
    mem_array.write_gds("cam_pram_layout.gds")
    print("Success! 'cam_pram_layout.gds' generated.")


