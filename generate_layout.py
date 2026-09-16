
import gdsfactory as gf

@gf.cell
def cam_pram_cell_grid():
    # Create a top-level blank chip component
    c = gf.Component("CAM_PRAM_ARRAY")
    
    # Define our components (Using Ring Resonators/Waveguides to simulate the optical links)
    led_surrogate = gf.components.straight(length=10, width=0.5)
    detector_surrogate = gf.components.straight(length=10, width=0.5)
    optical_path = gf.components.coupler_ring(radius=5, gap=0.2)

    # Generate a 4x4 memory cell array using layout loops
    spacing_x = 30
    spacing_y = 30

    for i in range(4):
        for j in range(4):
            # Calculate geometric coordinates for each memory cell
            x_pos = i * spacing_x
            y_pos = j * spacing_y
            
            # Place the emitter components programmatically
            led_ref = c << led_surrogate
            led_ref.move((x_pos, y_pos))
            
            # Place the optical routing/storage element
            path_ref = c << optical_path
            path_ref.move((x_pos + 10, y_pos + 5))
            
            # Place the detector arrays facing the direct line
            det_ref = c << detector_surrogate
            det_ref.move((x_pos + 20, y_pos))

    return c

if __name__ == "__main__":
    # Build the memory architecture layout
    mem_array = cam_pram_cell_grid()
    # Save as an industry-standard GDSII file for your repository
    mem_array.write_gds("hardware/cam_pram_layout.gds")
    print("Success! 'cam_pram_layout.gds' has been generated in the hardware folder.")
