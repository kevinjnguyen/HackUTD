//
//  ViewController.swift
//  HackUTD
//
//  Created by Kevin J Nguyen on 2/23/19.
//  Copyright © 2019 Kevin J Nguyen. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    let recycle_rep = RecycleRepository.shared

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        do {
            try recycle_rep.sendTestEcho()
        } catch {
            print("error")
        }
    }


}

