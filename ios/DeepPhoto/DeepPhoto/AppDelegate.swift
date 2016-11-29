//
//  AppDelegate.swift
//  DeepPhoto
//
//  Created by Daniel Velasco on 2016-11-15.
//  Copyright © 2016 Deep. All rights reserved.
//

import Cocoa
import "CameraExampleAppDelegate.h"
    
    @implementation CameraExampleAppDelegate
    
    @synthesize window = _window;
    
    - (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [self.window makeKeyAndVisible];
    return YES;
    }
    
    - (void)applicationWillResignActive:(UIApplication *)application {
    [[UIApplication sharedApplication] setIdleTimerDisabled:NO];
    }
    
    - (void)applicationDidEnterBackground:(UIApplication *)application {
    }
    
    - (void)applicationWillEnterForeground:(UIApplication *)application {
    }
    
    - (void)applicationDidBecomeActive:(UIApplication *)application {
    [[UIApplication sharedApplication] setIdleTimerDisabled:YES];
    }
    
    - (void)applicationWillTerminate:(UIApplication *)application {
    }
    
    end
    
    
}

