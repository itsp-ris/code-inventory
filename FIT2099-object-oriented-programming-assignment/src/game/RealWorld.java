package game;

import java.util.ArrayList;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.DoNothingAction;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.engine.Location;
import edu.monash.fit2099.engine.World;

public class RealWorld extends World {
	
	/**
	 * Constructor.
	 * 
	 * @param display the Display that will display this World.
	 */
	public RealWorld(Display display) {
		super(display);
	}
	
	/**
	 * Gives an Actor its turn.
	 *
	 * The Actions an Actor can take include:
	 * <ul>
	 * <li>those conferred by items it is carrying</li>
	 * <li>movement actions for the current location and terrain</li>
	 * <li>actions that can be done to Actors in adjacent squares</li>
	 * <li>actions that can be done using items in the current location</li>
	 * <li>skipping a turn</li>
	 * </ul>
	 *
	 * @param actor the Actor whose turn it is.
	 */
	@Override
	protected void processActorTurn(Actor actor) {
		if (actor.isConscious()) {
			super.processActorTurn(actor);
		} else {
			ActorSpecies actorSpecies = actor.getSpecies();
			GameMap map = actorLocations.locationOf(actor).map();
			
			Item corpse = new Food("dead " + actor, '%', actorSpecies.getActorNutrients(), 0, actorSpecies.getCorpseCost());
			map.locationOf(actor).addItem(corpse);
			
			Actions dropActions = new Actions();
			for (Item item : actor.getInventory())
				dropActions.add(item.getDropAction());
			for (Action drop : dropActions)		
				drop.execute(actor, map);
			map.removeActor(actor);
			
			display.println(actor + " " + "died of starvation");
		}
	}
	
	/**
	 * Returns true if the game is still running.
	 *
	 * The game is considered to still be running if the player is still around.
	 *
	 * @return true if the player is still on the map.
	 */
	@Override
	protected boolean stillRunning() {
		return actorLocations.contains(player) && player.isConscious();
	}
}
