//
//  HomeViewTableViewCell.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 13.05.2022.
//

import UIKit

class HomeViewTableViewCell: UITableViewCell {
   
    @IBOutlet weak var author: UILabel!
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet var bookImageView: UIImageView!
    
    override func awakeFromNib() {
        super.awakeFromNib()
    }
    
    public func configure(title: String?, author: String?){
        self.author.text = author
        self.nameLabel.text = title
    }
}
