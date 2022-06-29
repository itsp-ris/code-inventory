package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.GameMap;

/**
 * Special Action to quit game.
 */
public class QuitAction extends Action {
	
	/**
	 * Quit the game.
	 * @param actor The Actor performing the Action
	 * @param map 	The map the Actor is on
	 * @return a description of the Action suitable for feedback in the UI
	 */
	@Override
	public String execute(Actor actor, GameMap map) {
		actor.hurt(100);
		return menuDescription(actor);
	}
	
	/**
	 * A string describing the Action suitable for displaying in the UI menu.
	 * @param actor The actor performing the action.
	 * @return a String, e.g. "Player drops the potato"
	 */
	@Override
	public String menuDescription(Actor actor) {
		return actor + " " + "quits.";
	}

}
