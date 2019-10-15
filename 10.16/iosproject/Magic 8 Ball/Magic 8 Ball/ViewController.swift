//
//  ViewController.swift
//  Magic 8 Ball
//
//  Created by 木子 April on 2019/10/9.
//  Copyright © 2019 liujiaxin. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    let ballArray = ["ball1","ball2","ball3","ball4","ball5","ball6","ball7","ball8","ball9","ball10","ball11","ball12","ball13","ball14","ball15"]
    
    var randomBallNumber : Int = 0

    @IBOutlet weak var imageView: UIImageView!
    
    @IBAction func askButtonPressed(_ sender: UIButton) {
        newBallImage()
        print("press")
    }
    
    
    func newBallImage(){
        randomBallNumber = Int(arc4random_uniform(14))
        imageView.image = UIImage(named: ballArray[randomBallNumber])
    }
    
    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
            newBallImage()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
      newBallImage()
        
    }
    

}

