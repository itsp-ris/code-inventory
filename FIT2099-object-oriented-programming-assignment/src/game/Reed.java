package game;

import java.util.Random;

import edu.monash.fit2099.demo.conwayslife.Status;
import edu.monash.fit2099.engine.Exit;
import edu.monash.fit2099.engine.Ground;
import edu.monash.fit2099.engine.Location;

public class Reed extends Ground {
	private Random rand = new Random();
	private Status status = Status.ONGROUND;
	
	/**
	 * Constructor.
	 */
	public Reed() {
		super('!');
	}
	
	/**
	 * Inform the passage of time.
	 * @param location The location of the Ground 
	 */
	@Override
	public void tick(Location location) {
		generateFish(location);
		
		int count = 0;
		for (Exit exit : location.getExits()) {
			Location adjacent = exit.getDestination();
			
			if (adjacent.getGround() instanceof Reed) {
				count += 1;
				
				for (Exit adjExit : adjacent.getExits()) {
					Location farAdj = adjExit.getDestination();
					
					if (farAdj.getGround() instanceof Reed) {
						count += 1;
					}
				}
			}
		}
		
		if (count > 6) {
			status = Status.DEAD;
			location.setGround(new Water());
		}
	}
	
	/**
	 * Generate fish at this ground location
	 * @param location the location of the ground
	 * @return boolean
	 */
	private boolean generateFish(Location location) {
		if (rand.nextDouble() <= 0.1 && !location.containsAnActor()) {
			location.addActor(new Fish("Fish", '>', 0));
		}
		
		return false;
	}
}
