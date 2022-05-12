//
//  Course.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 12.05.2022.
//

import Foundation
import UIKit
import FirebaseDatabase


struct Course: Encodable {
    var id: Int
    var title: String
    var author: String
    var description: String
    var pictureUrl: String
    var categoryId: Int
    var isFavorite: Bool

    var dict: [String: Any] {
        return [
            "title": title,
            "author": author,
            "description": description,
            "picture_url": pictureUrl,
            "category": categoryId,
            "id": id,
            "isFavorite": isFavorite,
        ]
    }

    init?(snapshot: DataSnapshot) {
        if let value = snapshot.value as? [String: Any],
            let title = value["title"] as? String,
            let author = value["author"] as? String,
            let description = value["description"] as? String,
            let picture_url = value["picture_url"] as? String,
            let id = value["id"] as? Int,
            let categoryId = value["categoryId"] as? Int,
            let isFavorite = value["isFavorite"] as? Bool
        {
            self.title = title
            self.author = author
            self.description = description
            self.pictureUrl = picture_url
            self.id = id
            self.categoryId = categoryId
            self.isFavorite = isFavorite
        } else {
            return nil
        }
    }

}
