//
//  Category.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 12.05.2022.
//

import Foundation
import FirebaseDatabase

struct Category {
    var title: String
    var pictureUrl: String
    var id: Int
    
    var dict: [String: Any] {
        return [
            "title": title,
            "picture_url": pictureUrl,
            "id": id
        ]
    }

    init?(snapshot: DataSnapshot) {
        if let value = snapshot.value as? [String: Any],
            let title = value["title"] as? String,
            let picture_url = value["picture_url"] as? String,
            let id = value["id"] as? Int
        {
            self.title = title
            self.pictureUrl = picture_url
            self.id = id
        } else {
            return nil
        }
    }
    
}
