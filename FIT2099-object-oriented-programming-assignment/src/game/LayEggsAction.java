package game;

import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;

import edu.monash.fit2099.demo.conwayslife.Status;
import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Location;

/**
 * Special Action for laying Eggs.
 */
public class LayEggsAction extends Action {
	
	/**
	 * Lay Eggs.
	 * @param actor The Actor performing the Action
	 * @param map 	The map the Actor is on
	 * @return a description of the Action suitable for feedback in the UI
	 */
	@Override
	public String execute(Actor actor, GameMap map) {
		String result;
		
		String name = actor + "'s egg";
		
		
		Location here = map.locationOf(actor);
		try {
			Egg egg = new Egg(name, '*', actor.getClass().getDeclaredConstructor(String.class, int.class).newInstance(name, 0));
			here.addItem(egg);
			egg.setStatus(Status.ONGROUND);
		} catch (InstantiationException e) {
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			e.printStackTrace();
		} catch (IllegalArgumentException e) {
			e.printStackTrace();
		} catch (InvocationTargetException e) {
			e.printStackTrace();
		} catch (NoSuchMethodException e) {
			e.printStackTrace();
		} catch (SecurityException e) {
			e.printStackTrace();
		}
		
		result = actor + " " + "laid eggs.";
		return result;
	}

	/**
	 * A string describing the Action suitable for displaying in the UI menu.
	 * @param actor The actor performing the action.
	 * @return a String, e.g. "Player drops the potato"
	 */
	@Override
	public String menuDescription(Actor actor) {
		return actor + " " + "lay eggs.";
	}

}
